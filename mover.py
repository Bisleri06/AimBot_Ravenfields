import pyautogui
import time


def func():
			pyautogui.keyDown('a')
			pyautogui.keyDown('q')
			time.sleep(0.20)
			pyautogui.keyUp('a')
			pyautogui.keyUp('q')
			time.sleep(0.20)
			pyautogui.keyDown('d')
			pyautogui.keyDown('e')
			time.sleep(0.20)
			pyautogui.keyUp('d')
			pyautogui.keyUp('e')
			time.sleep(0.20)


try:
	while True:
			if pyautogui.position().x==1919:
				exit()

			pyautogui.keyDown('space')
			time.sleep(0.10)
			pyautogui.keyUp('space')
			time.sleep(0.10)
			#func()
			
except:

	exit()