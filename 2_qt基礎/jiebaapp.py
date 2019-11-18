# pyinstaller --add-data "dict.txt.big:." --add-data "idf.txt:./jieba/analyse" jiebaapp.py

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import sys
from jiebaui import Ui_MainWindow
import threading
import os
import jieba
if getattr(sys, 'frozen', False):
    dictpath = os.path.join(sys._MEIPASS, "dict.txt.big")
else:
    dictpath = "dict.txt.big"
jieba.set_dictionary(dictpath)
import jieba.analyse


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Text Analyzer")
        self.analysebtn.clicked.connect(self.analysethread)
        self.signal.connect(self.showresult)

    def analysethread(self):
        text = self.analysetext.toPlainText()
        threading.Thread(target=self.analyse, args=(text,)).start()

    def analyse(self, text):
        keywords = jieba.analyse.extract_tags(text)
        self.signal.emit("/".join(keywords))


    def showresult(self, text):
        self.resultlabel.setPlainText(text)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()