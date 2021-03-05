from pytube import YouTube
import os  
import shutil

cwd = os.getcwd()
videopath = cwd + '\\Videos'
## List of urls to download, seperated by commas
link=['https://www.youtube.com/watch?v=dQw4w9WgXcQ',  
    'https://www.youtube.com/watch?v=Zi_XLOBDo_Y'
    ] 

## Download video for each item in link
for url in link:  
	yt = YouTube(url)
	stream = yt.streams.first()
	video = stream.download()
	shutil.copy(video,videopath)
	os.remove(video)