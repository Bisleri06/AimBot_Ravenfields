import mss
from PIL import Image
import time
import pyautogui

counter=False

def test():
	with mss.mss() as sct:
		monitor={
					"top":420,
					"left":630,
					"width":570,
					"height":300,
		}

		sct_img=sct.grab(monitor)

		img = Image.new("RGB", sct_img.size)
		pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
		img.putdata(list(pixels))
		img.show()
			

test()

'''
with mss.mss() as sct:
	monitor={
				"top":420,
				"left":630,
				"width":600,
				"height":300,
	}

	while True:
			#pyautogui.press('space')
			#time.sleep(0.1)
			sct_img=sct.grab(monitor)

			img = Image.new("RGB", sct_img.size)
			pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
			img.putdata(list(pixels))
			for i in range(img.size[0]):
				for j in range(img.size[1]):
					counter=False
					dta=img.getpixel((i,j))
					if dta[0]>230 and dta[1]<40 and dta[2]<40:
						print("pixel: "+str(monitor["left"]+i)+" "+str(monitor["top"]+j))
						print("position: ",pyautogui.position())
						pyautogui.moveTo(monitor["left"]+i+15,monitor["top"]+j+5)
						counter=True
						break
				
				if counter==True:
					break
'''