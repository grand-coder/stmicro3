from tkinter import *
from jieba.analyse import extract_tags

class MyFrame(LabelFrame):
    def __init__(self, master):
        # 重要習慣
        LabelFrame.__init__(self, master, text="請吃新聞")
        self.news = Text(self, height=10)
        self.news.pack(expand=True, fill=BOTH, padx=20, pady=20)
        self.b1 = Button(self, text="分析", command=self.analyse)
        self.b1.pack(expand=True, fill=BOTH, padx=20, pady=20)
        self.result = Label(self, text="按就有分析結果")
        self.result.pack(expand=True, fill=BOTH, padx=20, pady=20)

    def analyse(self):
        news = self.news.get("1.0", "end")
        keywords = extract_tags(news, 5)
        self.result["text"] = str(keywords)

window = Tk()
f1 = MyFrame(window)
f1.pack(expand=True, fill=BOTH, padx=40, pady=40)
# "寬x高+起始x座標+起始y座標"
window.geometry("500x500+200+200")
window.mainloop()