# coding:utf8
from selenium import webdriver

from homework.task2.str_util import get_width, get_str_width

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# driver.implicitly_wait(1)
# 抓取排行榜信息

driver.get('http://music.baidu.com/top/new')

# 层层往下查找
div = driver.find_element_by_id("songListWrapper")
ul = div.find_element_by_tag_name("ul")
liList = ul.find_elements_by_tag_name('li')

for li in liList:
    # 哪些 是有 有up 标签的 歌曲， F12 查看特性
    upTags = li.find_elements_by_class_name("up")
    if upTags:
        # 由于只要 歌曲名和 演唱者名
        title = li.find_element_by_class_name("song-title")
        titleStr = title.find_element_by_tag_name("a").text

        authorsStr = li.find_element_by_class_name("author_list").text

        pad_len = 31 - (len(titleStr.encode()))+len(titleStr)
        # print(pad_len)
        print('{0:<{1}}\t:{2:<}{3:<}'.format(titleStr, pad_len,' '*8,authorsStr))

driver.quit()
