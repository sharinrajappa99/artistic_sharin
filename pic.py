#pic.py
import os

def takepic():
	os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/cl215/sharin/temp.jpg")
	print("pic taken ")
	return
takepic()	
