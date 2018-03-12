import cv2
import numpy as np
from threading import Thread
from playsound import playsound

cap = cv2.VideoCapture(1)
k = True

ret, t0 = cap.read()
ret, t1 = cap.read()
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)

while True:
	t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
	diff = cv2.absdiff(t1, t0)
	ret,threshold_image = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	cymbal = cv2.countNonZero(threshold_image[230:360,30:180])
	big = cv2.countNonZero(threshold_image[300:360,325:385])
	medium = cv2.countNonZero(threshold_image[100:150,420:475])
	small = cv2.countNonZero(threshold_image[165:200,215:265])
	if cymbal>3000:
		if k:
			Thread(target = playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')).start()
			#playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')

	if big>500:
		if k:
			Thread(target = playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')).start()

	if medium>500:
		if k:
			Thread(target = playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')).start()

	if small>500:
		if k:
			Thread(target = playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')).start()

	k = not k
	cv2.imshow('Window', threshold_image)

	t0 = t1
	ret, t1 = cap.read()	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
