import os
import ctypes
import random
import threading
from ctypes import wintypes
from PIL import Image, ImageDraw, ImageFont



def printit():
	# Creating Thread 
	threading.Timer(5.0, printit).start()
	
	text = ["Success is not final; failure \nis not fatal: It is the courage to \ncontinue that counts.", 
	"It is better to fail in originality \nthan to succeed in imitation.", 
	"The road to success \nand the road to failure are \nalmost exactly the same.", 
	"Success usually comes to those \nwho are too busy to be looking for it.",  
	"Opportunities don't happen. \nYou create them.", 
	"Don't be afraid to give up\n the good to go for the great.", 
	"I find that the harder \nI work, the more luck I seem to have.", 
	"There are two types of people who \nwill tell you that you cannot make\n a difference in this world: \nthose who are afraid to try and those who are \nafraid you will succeed.",
	 "Successful people do what unsuccessful \npeople are not willing to do. \nDon't wish it were easier; \nwish you were better.", 
	 "Try not to become a man of success. \nRather become a man of value."]
	
	val = random.randint(0, len(text))

	# Generating Wallpaper
	img = Image.new('RGB', (1920, 1080), color = (960, 109, 137))
	fnt = ImageFont.truetype('font/Rubik-Black.ttf', 72)
	d = ImageDraw.Draw(img)
	d.text((350,400), text[val], font=fnt, fill=(255, 255, 0))
	 
	img.save('midi turmes.png')

	# Changing Wallpaper
	drive = "c:\\"
	folder = "test"
	image = "midi turmes.png"
	image_path = os.path.join(drive, folder, image)

	SPI_SETDESKWALLPAPER  = 0x0014
	SPIF_UPDATEINIFILE    = 0x0001
	SPIF_SENDWININICHANGE = 0x0002

	user32 = ctypes.WinDLL('user32')
	SystemParametersInfo = user32.SystemParametersInfoW
	SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
	SystemParametersInfo.restype = wintypes.BOOL
	print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))
	print(val)

printit()
	
	

