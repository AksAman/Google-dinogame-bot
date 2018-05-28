# from __future__ import pyscreenshot as ss
import pyscreenshot as ss
import pyautogui
import time
import cv2 as cv
import numpy as np
from PIL import ImageOps

sumThreshold=1516
imgEnd=0

class Coordinates():
	restartBtn=(388.8,436.2)
	dinoTop=(210,440)

	# TreeBox X=235.5
	# Lowest Obstacle Y=451.4


def restartGame():
	pyautogui.click(Coordinates.restartBtn)


def pressSpace():
	pyautogui.keyDown('up')
	print "jump"
	time.sleep(0.05)
	pyautogui.keyUp('up')


def imageGrab():
	# box=(Coordinates.dinoTop[0]+15,Coordinates.dinoTop[1],Coordinates.dinoTop[0]+70,Coordinates.dinoTop[1]+35)
	# box=((240,435,50,40))
	# img=pyautogui.screenshot(region=(240,435,50,40))
	# imgArray=np.array(img)
	box=(228,440,228+47,440+27)
	img=ss.grab(box)
	grayscale=ImageOps.grayscale(img)
	imgArray=np.array(grayscale.getcolors())
	# grayscale=cv.cvtColor(imgArray,cv.COLOR_BGR2GRAY)
	# (thresh, im_bw) = cv.threshold(grayscale, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
	global imgEnd 
	imgSum=imgArray.sum()
	if(imgSum>sumThreshold):
		# fName="im"
		img.show()
		# imgEnd+=1
	print imgSum
	return imgSum

# 

# pressSpace()
def main():
	while True:
		# imageGrab()
		if(imageGrab()>sumThreshold):
			pressSpace()
			time.sleep(0.1)

restartGame();
main()

    

