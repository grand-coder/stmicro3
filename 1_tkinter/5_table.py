from tkinter import *
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText

class InputFrame(LabelFrame):
    def __init__(self, root, **kwargs):
        LabelFrame.__init__(self, root, text="輸入資訊", padx=20, pady=20)
        self.name_label = Label(self, text="餐廳名字:")
        self.name_label.pack()
        self.name_input = Entry(self)
        self.name_input.pack()
        self.price_label = Label(self, text="餐廳價錢:")
        self.price_label.pack()
        self.price_input = Entry(self)
        self.price_input.pack()
        self.comment_label = Label(self, text="餐廳心得:")
        self.comment_label.pack()
        self.comment_input = Text(self, height=3,
                                  width=30,
                                  bg="#D3D3D3",
                                  highlightcolor="#6495ED")
        self.comment_input.pack()


class ShowFrame(LabelFrame):
    def __init__(self, root, **kwargs):
        LabelFrame.__init__(self, root, text="儲存餐廳", padx=20, pady=20)
        self.tree = Treeview(self, columns=['1', '2', '3'],
                             show='headings')
        self.tree.column('1', width=100, anchor='center')
        self.tree.column('2', width=100, anchor='center')
        self.tree.column('3', width=100, anchor='center')
        self.tree.heading('1', text='餐廳')
        self.tree.heading('2', text='價錢')
        self.tree.heading('3', text='心得')
        self.tree.insert('', 'end', values=["周", "R10", "Male"])
        self.tree.pack(expand=True, fill=BOTH)


window = Tk()
f1 = InputFrame(window)
f1.pack(side=LEFT, ipadx=20, ipady=20, padx=10, pady=10, fill=BOTH, expand=True)
f2 = ShowFrame(window)
f2.pack(side=LEFT, ipadx=20, ipady=20, padx=10, pady=10, fill=BOTH, expand=True)
window.mainloop()