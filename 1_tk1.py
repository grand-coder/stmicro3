import tkinter as tk
from jieba.analyse import extract_tags

def analyse():
    global t1
    global result
    news = t1.get("1.0", "end")
    keys = extract_tags(news, 5)
    result["text"] = str(keys)


window = tk.Tk()
window.title("First App")
window.geometry("500x500+250+250")

# 名字 = 元件(父親)
# 名字.排版() [pack, grid]
f1 = tk.Frame(window)
f1.pack(padx=20, pady=20)
l1 = tk.Label(f1, text="請輸入文章")
l1.pack()
t1 = tk.Text(f1)
t1.pack()
b1 = tk.Button(f1, text="分析", command=analyse)
b1.pack(expand=True, fill=tk.BOTH)
result = tk.Label(f1, text="請點按鈕分析")
result.pack()


window.mainloop()