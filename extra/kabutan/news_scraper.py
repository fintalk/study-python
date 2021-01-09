"""
[株探 | 決算速報](https://kabutan.jp/news/?page=1) をスクレイピングする。

1. https://kabutan.jp/news/?page=1 をスクレイピングしてニュース一覧だけ取得する
1. URLを取得して、まだフェッチしていないページがあればフェッチして、ファイルに書き出す


"""
from pprint import pprint
import requests 
from bs4 import BeautifulSoup

def get_news_detail(tr):
    """
    tr: １ニュースの soup object
    """
    dt = tr.select_one("td.news_time").select_one("time").get("datetime")
    url = "https://kabutan.jp" + tr.select_one("a").get("href")
    text = tr.select_one("a").getText() 
    code = tr.select_one("td.oncodetip_code-data1").get("data-code")
    category = tr.select("td")[1].get("class")
    if "ctg3_kk" in category:
        category = "earnings"
    elif "ctg3_ks" in category:
        category = "amended"
    else:
        category = "anything"
    return {
        "datetime":dt,
        "url":url, 
        "text":text,
        "code":code, 
        "category":category
    }

def get_news_tables(soup):
    return soup.select("table.s_news_list")

def get_news_list(tables):
    results = list()
    for table in tables: 
        for tr in table.select("tr"):
            results.append(get_news_detail(tr))
    return results

if __name__ == "__main__":
    print("START")
    url = "https://kabutan.jp/news/?page=1"
    res = requests.get(url)
    
    assert res.status_code ==200, "Status Code {}".format(res.status_code)
    
    soup = BeautifulSoup(res.content, "html.parser")
    tables = get_news_tables(soup)
    results = get_news_list(tables)
    pprint(results)


