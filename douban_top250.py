from selenium import webdriver
import requests
import pandas as pd
from bs4 import BeautifulSoup


url_list = ["https://movie.douban.com/top250",
    "https://movie.douban.com/top250?start=25&filter=",
    "https://movie.douban.com/top250?start=50&filter=",
    "https://movie.douban.com/top250?start=75&filter=",
    "https://movie.douban.com/top250?start=100&filter=",
    "https://movie.douban.com/top250?start=125&filter=",
    "https://movie.douban.com/top250?start=150&filter=",
    "https://movie.douban.com/top250?start=175&filter=",
    "https://movie.douban.com/top250?start=200&filter=",
    "https://movie.douban.com/top250?start=225&filter="
            ]

url = "https://movie.douban.com/top250"
name = []
score = []

def open_url(url_list):
    browser = webdriver.Chrome()
    for i in url_list:
        browser.get(i)


def read_page(url):
    con = requests.get(url)
    content = BeautifulSoup(con.content, "lxml")
    # content = content.find("div", class_="content")
    for i in content.find_all("div", class_ = "hd"):
        list = i.find_all("span", class_="title")
        name.append(list[0].string)
    for j in content.find_all("div", class_="star"):
        l = j.find_all("span")
        if len(l) == 4:
            score.append(l[1].string)
    # print(len(name))
    # print(len(score))
    write_csv(name, score)
    return

def write_csv(list, list2):
    dataframe = pd.DataFrame({'name':list, 'score':list2})
    dataframe.to_csv("F://movie.csv", index=False, sep=',', encoding="utf_8_sig")
    return
if __name__ == "__main__":
    for url in url_list:
        # print(url)
        a = read_page(url)
