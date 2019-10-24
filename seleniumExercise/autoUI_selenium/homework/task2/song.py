from selenium import  webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('http://music.baidu.com/top/new')
#获取html
html = driver.page_source

soup = BeautifulSoup(html,'html5lib')

for i in soup.find_all('div',class_='song-item'):
    if i.find('i',class_='up'):
        song_name = (i.find('span',class_='song-title').text).strip()
        singer = (i.find('span',class_='singer').text).strip()
        '''
        汉字字符与英文占字节不一致，输出结果看的不美观
        print('{:<30}:{:>}'.format(song_name,singer))
        '''
        #强迫症，对齐输出
        print('{name:<{len}}\t:\033[31;0m{singer}\033[0m'.format(name=song_name ,
           len=31 - len(song_name.encode('gbk')) + len(song_name),singer=singer))

driver.quit()






