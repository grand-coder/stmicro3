# a = 元件(指定老爸是誰)
# a.排版(pack, grid)
from tkinter import *

def bmi():
    global e1
    global e2
    global result
    try:
        height = float(e1.get())
        weight = float(e2.get())
        bmi = weight / (height / 100) ** 2
        result["text"] = bmi
    except ValueError:
        result["text"] = "你肯定又在亂打!!!"


window = Tk()
# Frame:圖層
f1 = Frame(window)
f1.pack()
# Label: 標籤(不能輸入)
l1 = Label(f1, text="輸入身高")
l1.pack()
# Entry: 單行輸入
e1 = Entry(f1)
e1.pack()

l2 = Label(f1)
l2["text"] = "輸入體重"
l2.pack()

# Entry: 單行輸入
e2 = Entry(f1)
e2.pack()

# Button
b1 = Button(f1, text="計算", bg="red", command=bmi)
b1.pack(expand=True, fill=BOTH)

result = Label(f1)
result.pack()

window.mainloop()