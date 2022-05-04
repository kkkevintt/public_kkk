# 抓取PTT八卦版原始碼(HTML)
import urllib.request as req
def getData(url):
#建立一個request物件\ 告訴他我已按過
    request = req.Request(url, headers = {
        "cookie":"over18=1",
        "User-Agent":"ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    })#看起來像是普通使用者 
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")   #我們網路上抓下來的資料原始碼 
    #解析原始碼，取得每天文章標題 
    import bs4 
    root = bs4.BeautifulSoup(data, "html.parser")#用BS4套件工具
    titles = root.find_all("div",class_="title")#尋找所有div 標籤class=title條件 
    for title in titles:
        if title.a != None:
            print(title.a.string)
    #抓取上一頁連結(動態) 利用bs4工具 尋找a 標籤
    nextlink = root.find("a",string = "‹ 上頁")#找到內文是‹ 上頁 的a 標籤
    return nextlink["href"]#屬性
#主程序:抓取一個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0 
while count<3:
    pageURL= "https://www.ptt.cc"+getData(pageURL)
    count += 1 