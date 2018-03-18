import cv2
import numpy as np
from threading import Thread
import threading
from playsound import playsound
import pygame
import time

pygame.init()
pygame.mixer.init()

delay = 0.25
time1=time.time()
time2=time.time()
time3=time.time()
time4=time.time()
time5=time.time()
time6=time.time()
time7=time.time()
time8=time.time()
k1=True
k2=True
k3=True
k4=True

def drum1(time1,time):
	if deftime(time1,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/thaal.ogg').play()
		#time.sleep(2)	

def drum2(time2,time):
	if deftime(time2,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/motha.ogg').play()
		#time.sleep(2)	

def drum3(time3,time):
	if deftime(time3,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/drum1.ogg').play()
		#time.sleep(2)	

def drum4(time4,time):
	if deftime(time4,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/motha.ogg').play()
		#time.sleep(2)	

def arcreactersound(time5,time):
	if deftime(time5,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/friends_theme_song.ogg').play()
		#time.sleep(2)

def hammersound(time6,time):
	if deftime(time6,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/albatroz.ogg').play()
		#time.sleep(2)

def dhaalsound(time7,time):
	if deftime(time7,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/tuntun.ogg').play()
		#time.sleep(2)

def spidersound(time8,time):
	if deftime(time8,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/motha.ogg').play()
		#time.sleep(2)


def deftime(t1,t2):
	return t2-t1

cap = cv2.VideoCapture(0)
k = True

ret, t0 = cap.read()
ret, t1 = cap.read()
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)

while True:
	t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
	diff = cv2.absdiff(t1, t0)
	ret,threshold_image = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	cymbal = cv2.countNonZero(threshold_image[130:260,30:180])
	big = cv2.countNonZero(threshold_image[200:260,315:375])
	medium = cv2.countNonZero(threshold_image[5:45,415:470])
	small = cv2.countNonZero(threshold_image[65:100,205:255])
	arcreacter = cv2.countNonZero(threshold_image[320:360,455:505])
	hammer = cv2.countNonZero(threshold_image[240:280,500:545])
	dhaal = cv2.countNonZero(threshold_image[155:185,480:525])
	spider = cv2.countNonZero(threshold_image[105:135,435:465])
	
	if k:
		if cymbal>1000:
			Thread(target = drum1(time1,time.time())).start()
			time1=time.time()
			#playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')
		if big>100:
			Thread(target = drum2(time2,time.time())).start()

		if medium>100:
			Thread(target = drum3(time3,time.time())).start()

		if small>100:
			Thread(target = drum4(time4,time.time())).start()

		if arcreacter>100:
			thread_arcreactor = Thread(target = arcreactersound(time5,time.time())).start()


		if hammer>100:
			Thread(target = hammersound(time6,time.time())).start()

		if dhaal>100:
			Thread(target = dhaalsound(time7,time.time())).start()

		if spider>100:
			Thread(target = spidersound(time8,time.time())).start()


	k = not k
	cv2.imshow('Window', threshold_image)

	t0 = t1
	ret, t1 = cap.read()	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
