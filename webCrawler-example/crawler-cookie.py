# 抓取 ptt 電影版網頁原始碼
import urllib.request as req
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 建立一個Request物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 解析原始碼
# 安裝套件 pip3 install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSop 協助解析 HTML 格式文件
titels=root.find_all("div", class_="title")
for titel in titels:
    if titel.a != None:
        print(titel.a.string)

nextLink=root.find("a", string="‹ 上頁")
# print(nextLink)
# <a class="btn wide" href="/bbs/Gossiping/index39082.html">‹ 上頁</a>
print(nextLink["href"])