import os
import shutil

cwd = os.getcwd()
audiopath = cwd + '\\Audio'
for file in os.listdir(cwd):
	if file.endswith('.mp3'):
		shutil.copy(file, audiopath)
		os.remove(file)