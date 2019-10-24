#-*- coding:utf-8 -*-
# @Time  :2019/6/4 10:47
'''
需求：
1、打开百度新歌榜， http://music.baidu.com/top/new
2、在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者
3、注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉
'''
#------------------------------------------------------------方法一：直接使用selenium
from selenium import webdriver
def songParse(songitem):
    pass
driver=webdriver.Chrome('F:\selenium\driver\chromedriver.exe')
driver.get('http://music.baidu.com/top/new')
song_items=driver.find_elements_by_class_name('song-item')
for one in song_items:
    status=one.find_element_by_class_name('status').find_element_by_tag_name('i').get_attribute('class')
    song_title=one.find_element_by_class_name('song-title ').text.split('（')[0]
    singer=one.find_element_by_class_name('singer').text
    if status == 'up':
        print('%-15s：\t%-s'%(song_title,singer))

driver.quit()

#------------------------------------------------------------方法二：使用selenium结合BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome('F:\selenium\driver\chromedriver.exe')
driver.get('http://music.baidu.com/top/new')
with open('musictop.html','w',encoding='utf8') as fw:
    fw.write(driver.page_source)

with open('musictop.html','r',encoding='utf8') as f:
    html_doc=f.read()
soup=BeautifulSoup(html_doc,'html5lib')
song_items=soup.findAll('div',class_='song-item')
for one in song_items:
    status=one.find('span',class_='status').i['class'][0]
    song_title=one.find('span',class_='song-title').get_text().split('（')[0]
    singer=one.find('span',class_='singer').get_text().strip()
    if status == 'up':
        print('%-15s：\t%-s'%(song_title,singer))
driver.quit()



