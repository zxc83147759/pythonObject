import os
import subprocess
import pytube
url='https://www.youtube.com/watch?v=1YCInueffWc'
yt = pytube.YouTube(url)

print('影片名稱：',yt.title)
print('影片介紹：',yt.description)
print('影片觀看次數：',yt.views)
print('影片下載位置：',yt.streams.first().download('E:/test'))
