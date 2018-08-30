from SpotifyWebAPI import Track_name,Album_name,Artist_name,Image_links,Release_date,num,Track_length
from selenium import webdriver
from webbot import Browser
import webbot.drivers as wb
import driver_builder
import time
from mutagen.mp3 import MP3
import os
from winreg import *
#TODO Make downloading work with headless chrome
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    downloadir = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
web = Browser(showWindow=False)
print(driver_builder.DriverBuilder._get_chrome_driver(self= driver_builder.DriverBuilder,download_location=downloadir,headless=False))
def youtube(num):
    for i in range(num):
        web.go_to('mp3juices.cc')
        web.click(id='query')
        web.type(str(Track_name[i]) + ' ' + str(Artist_name[i] + ' ' + 'audio'))
        web.press(web.Key.ENTER)
        web.click("Download")
        time.sleep(4)
        web.click(classname="url")
        print(str(round((i/num)*100,2)) + '%...')
    print("Finished")
    create_folder()
def create_folder():
    try:
        os.mkdir(r'C:\Users\Lazyw\Music\SpotifyPlaylist')

        print("Put music files into SpotifyPlaylist folder")
    except FileExistsError:
        print("Folder Already exists")
        print("Put music files into SpotifyPlaylist folder")
def metadata_check():
    for i in range (num):
        dir_path= os.listdir(r'C:\Users\Lazyw\Music\SpotifyPlaylist')
        audiofile= MP3('C:\\Users\\Lazyw\\Music\\SpotifyPlaylist\\' + dir_path[i])
        print(dir_path[i])
        print(sorted(Track_name)[i])
        length = audiofile.info.length
        length -= 0.1
        if length[i]-5 < Track_length[i] and length[i]+5>Track_length[i]:
            print('hello')
        audiofile["title"] = Track_name[i]

if input("download(1) or fix metadata(2)") == '1':
    youtube(num)
else:
    metadata_check()