import pyautogui
import sys
import time
width, height = pyautogui.size()

def main():
	if width != 1920 and height !=1080:
		print "Invalid resolution. Only 1080p currently supported. "
		return
	killerSlash = (1354,986)
	red = (240,0,0)
	gray = (93,90,85)
	black = (0,0,0)
	readpos = (1770,1000)
	slashPos = [(1383,971)]
	ourSlash = slashPos[0]
	while True:
		if pyautogui.pixelMatchesColor(ourSlash[0], ourSlash[1], gray):
			pyautogui.click(x=readpos[0], y=readpos[1])
		elif pyautogui.pixelMatchesColor(ourSlash[0], ourSlash[1], black, tolerance=20):
			while pyautogui.pixelMatchesColor(ourSlash[0], ourSlash[1], black, tolerance=20):
				time.sleep(1)
			if pyautogui.pixelMatchesColor(killerSlash[0], killerSlash[1], red) or pyautogui.pixelMatchesColor(killerSlash[0], killerSlash[1], gray):
				return
			if pyautogui.pixelMatchesColor(killerSlash[0], killerSlash[1], black):
				continue
			
		time.sleep(1)

if __name__ == '__main__':
  main()
	