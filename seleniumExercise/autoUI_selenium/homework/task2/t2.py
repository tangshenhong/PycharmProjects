from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://music.baidu.com/top/new')

div=driver.find_element_by_id('songListWrapper')
ul=div.find_element_by_tag_name('ul')
song_list=ul.find_elements_by_tag_name('li')


# for song in song_list:
#     status=song.find_element_by_class_name('song-item').find_element_by_class_name('status').find_element_by_tag_name('i').get_attribute('class')
#     if status =='up':
#         song_title=song.find_element_by_class_name('song-item').find_element_by_class_name('song-title ').text
#         singer=song.find_element_by_class_name('song-item').find_element_by_class_name('singer ').text
#         print('{}:\t{}'.format(song_title,singer))


statu=driver.find_elements_by_css_selector('#songListWrapper div ul li div.song-item span.status i')    #.get_attribute('class')
#print([u.get_attribute('class') for u in statu])
statu_list=[u.get_attribute('class') for u in statu]
for num,sta in enumerate(statu_list):
    if sta =='up':
        song_tit=driver.find_elements_by_css_selector('#songListWrapper div ul li div.song-item span.song-title a')
        singer=driver.find_elements_by_css_selector('#songListWrapper div ul li div.song-item span.author_list a')
        print('{}:\t{}'.format(song_tit[num].text,singer[num].text))


driver.quit()


















    # songlist=driver.find_element_by_id('songListWrapper').find_elements_by_class_name('song-item')
#
# for song in songlist:
#     status= song.find_element_by_class_name('status').find_element_by_tag_name('i')
#     if status.get_attribute('class')=='up':
#         song_title=song.find_element_by_class_name('song-title').text
#         singer=song.find_element_by_class_name('singer').text
#         print('{}<10:\t{}'.format(song_title,singer))

driver.quit()