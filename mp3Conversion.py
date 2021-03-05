import os
from pydub import AudioSegment
import shutil

files = []
cwd = os.getcwd()
videopath = cwd + '\\Videos\\'									## Set directory path containing video files
directory = os.listdir(videopath)

print(directory)

for file in directory:
	if file.endswith('.mp4'):
		filename = file.replace('.mp4','.mp3')
		mp4audio = AudioSegment.from_file(videopath+file, 'mp4')	
		mp3audio = mp4audio.export(filename, format = 'mp3')
		os.remove(videopath+file)								## Delete source mp4 file