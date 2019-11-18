from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import glob
import json
import threading
import subprocess
import os
import sys

if getattr(sys, 'frozen', False):
    qt_creator_file = os.path.join(sys._MEIPASS, "command.ui")
    default_project = os.path.join(sys._MEIPASS, "test")
else:
    qt_creator_file = "command.ui"
    default_project = "test"


# 直接使用.ui檔案
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

# Model
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, project=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.project = project
        self.commands = []
        for fn in glob.glob("{}/*.ci".format(project)):
            bn = os.path.basename(fn)
            self.commands.append(bn.replace(".ci", ""))

    def add_data(self, n):
        if n:
            # begin和end在做完以後會幫你發射signal
            self.beginInsertRows(QtCore.QModelIndex(),
                                 len(self.commands),
                                 len(self.commands))
            self.commands.append(n)
            self.endInsertRows()
            return self.index(len(self.commands)-1, 0)

    def delete_data(self, n):
        self.beginRemoveRows(QtCore.QModelIndex(),
                                 n,
                                 n)
        os.remove("{}/{}.ci".format(self.project, self.commands[n]))
        del self.commands[n]
        self.endRemoveRows()

    # 這兩個是必覆蓋的兩個command
    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.commands[index.row()]
            return text

    def rowCount(self, index):
        return len(self.commands)



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Smart Command")
        self.model = TodoModel(project=default_project)
        self.commandlist.setModel(self.model)
        (self.commandlist.selectionModel()
                         .currentChanged
                         .connect(self.showcmd))
        self.newcommandbtn.clicked.connect(self.savenewcmd)
        self.savecommandbtn.clicked.connect(self.savecmd)
        #self.execcommandbtn.clicked.connect(self.execcmd)
        # SIGNAL&SLOT
        self.execcommandbtn.clicked.connect(self.start)

        self.signal.connect(self.execcmd)
        # 設置右鍵
        self.commandlist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.commandlist.customContextMenuRequested.connect(self.right)

    def start(self):
        threading.Thread(target=self.work).start()

    def work(self):
        cmd = self.getcommand()
        result = subprocess.run("{} {}".format(cmd["command"],
                                                cmd["param"]),
                                shell=True, stdout=subprocess.PIPE)
        try:
            text = result.stdout.decode("utf-8")
        except:
            text = result.stdout.decode("BIG5")
        self.signal.emit(text)

    def savenewcmd(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self,
                                                     "Save File",
                                                     default_project,
                                                     "Command(*.ci)")
        if not name[0] == "":
            file = open(name[0], 'w')
            json.dump(self.getcommand(), file)
            file.close()
        base = os.path.basename(name[0]).replace(".ci", "")
        i = self.model.add_data(base)
        self.commandlist.setCurrentIndex(i)


    def savecmd(self):
        row = self.commandlist.selectionModel().currentIndex()
        fn = "{}.ci".format(row.data())
        with open(os.path.join(default_project, fn), "w", encoding="utf-8") as f:
            json.dump(self.getcommand(), f)


    def showcmd(self, current, previous):

        fn = "{}.ci".format(current.data())
        with open(os.path.join(default_project, fn), encoding="utf-8") as f:
            data = json.load(f)
        self.usageinput.setText(data["usage"])
        self.commandinput.setText(data["command"])
        self.paraminput.setText(data["param"])
        self.moreinput.setText(data["more"])

    def getcommand(self):
        return {"usage":self.usageinput.text(),
                "command":self.commandinput.text(),
                "param":self.paraminput.text(),
                "more":self.moreinput.toPlainText()}

    def execcmd(self, result):
        self.showresult.setPlainText(result)

    def right(self, QPos):
        self.listMenu = QtWidgets.QMenu()
        menu_item = self.listMenu.addAction("刪除")
        menu_item.triggered.connect(self.menuItemClicked)
        parentPosition = self.commandlist.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show()

    def menuItemClicked(self):
        row = self.commandlist.selectionModel().currentIndex()
        self.model.delete_data(row.row())

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()