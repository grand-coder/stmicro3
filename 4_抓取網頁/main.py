import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# Pandas
import pandas as pd

page = 59
# Pandas
total = {
    "評分":[],
    "日文":[],
    "英文":[],
    "詳細":[]
}
while True:
    print("頁數:", page)
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print("網址:", url)
    try:
        response = urlopen(url)
    except HTTPError:
        # Pandas
        order = ["評分", "日文", "英文", "詳細"]
        df = pd.DataFrame(total,
                          columns=order)
        df.to_csv("tabelog.csv",
                  encoding="utf-8",
                  index=False)
        print("http錯誤, 可能是最後一頁")
        break
    html = BeautifulSoup(response)

    rs = html.find_all("li", class_="list-rst")
    for r in rs:
        en = r.find("a", class_="list-rst__name-main")
        ja = r.find("small", class_="list-rst__name-ja")
        rate = r.find("b", class_="c-rating__val")
        prices = r.find_all("span", class_="c-rating__val")

        print(rate.text, ja.text, en.text)
        print("晚間價錢:", prices[0].text)
        print("午間價錢:", prices[1].text)
        print(en["href"])
        # Pandas
        total["評分"].append(rate.text)
        total["日文"].append(ja.text)
        total["英文"].append(en.text)
        total["詳細"].append(en["href"])

    page = page + 1

