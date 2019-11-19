import tkinter as tk
from jieba.analyse import extract_tags
import time
import threading

class CustomFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.l1 = tk.Label(self, text="請輸入文章")
        self.l1.pack()
        self.t1 = tk.Text(self)
        self.t1.pack()
        self.b1 = tk.Button(self,
                            text="分析",
                            command=self.analyse_thread)
        self.b1.pack(expand=True, fill=tk.BOTH)
        self.result = tk.Label(self, text="請按按鈕")
        self.result.pack()

    def analyse_thread(self):
        news = self.t1.get("1.0", "end")
        thread = threading.Thread(target=self.analyse,
                                  args=(news, ))
        thread.start()

    def analyse(self, text):
        self.b1["state"] = tk.DISABLED
        time.sleep(5)
        keys = extract_tags(text, 5)
        self.result["text"] = str(keys)
        self.b1["state"] = tk.ACTIVE

window = tk.Tk()
window.title("First App")
window.geometry("500x500+250+250")

f1 = CustomFrame(window)
f1.pack(padx=20, pady=20)

window.mainloop()