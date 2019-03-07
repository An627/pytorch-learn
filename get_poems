from selenium import webdriver
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

pname = []
u= "https://so.gushiwen.org"
url = "https://so.gushiwen.org/gushi/shijing.aspx"
url_list = []
pintroduction = []
pcontent =[]

def get_herf(url):
    con = requests.get(url)
    content = BeautifulSoup(con.content, "lxml")
    for i in content.find_all("div", class_="typecont"):
        list = i.find_all("span")
        for j in range(len(list)):
            herf = str(list[j])
            # 通过正则表达式截取相应的字符
            p = "\"/.+?\""
            pattern = re.compile(p)
            if len(herf) > 41:
                new = pattern.findall(herf)
                url_list.append(new[0].replace("\"", ""))
            #  简单的方法，通过找到某个字符的前两个下标进行截取
            # index = herf.find("\"")
            # index1 = herf.find("\"", index+1)
            # if len(herf) > 41:
            #     url_list.append(herf[15:41])
    # print(url_list)
    return url_list
def get_poems(url):
    p = "[\u4e00-\u9fa5。：，？！]+"
    pattern = re.compile(p)
    con = requests.get(url)
    content = BeautifulSoup(con.content, "lxml")  # 解析html内容
    c = content.find("div", class_="sons")
    # print(str(c))
    n = c.find("h1").string  # 诗歌名称
    intr = str(c.find("p", class_="source"))  # 诗歌介绍数组
    cont = str(c.find("div", class_="contson"))  # 诗词内容数组
    intro = "".join(pattern.findall(intr))  # 转换为诗歌介绍字符串
    conte = "".join(pattern.findall(cont))  # 转换为诗词内容字符串
    pname.append(n)
    pintroduction.append(intro)
    pcontent.append(conte)
    # print(pname)
    return pname, pintroduction, pcontent

def write_csv(list, list2, list3):
    dataframe = pd.DataFrame({'name':list, 'introduction':list2, 'content':list3})
    dataframe.to_csv("F://poems.csv", index=False, sep=',', encoding="utf_8_sig")
    return



if __name__ == "__main__":
    url_list = get_herf(url)
    for i in url_list:
        newu = u + str(i)
        get_poems(newu)
        print(newu, "已完成！")
    write_csv(pname, pintroduction, pcontent)
