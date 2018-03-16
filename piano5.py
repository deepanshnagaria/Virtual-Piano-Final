import cv2
import numpy as np
from threading import Thread
from playsound import playsound
import threading
#from piano_thread import WebcamVideoStream
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
time9=time.time()
time10=time.time()
time11=time.time()
time12=time.time()
time13=time.time()
time14=time.time()
def sound1(time1,time):
	if deftime(time1,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
		#time.sleep(0.1)	

def sound2(time2,time):
	if deftime(time2,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1s.wav').play()
		#time.sleep(2)	

def sound3(time3,time):
	if deftime(time3,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/b1.wav').play()
		#time.sleep(2)	

def sound4(time4,time):
	if deftime(time4,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1.wav').play()
		#time.sleep(2)	

def sound5(time5,time):
	if deftime(time5,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1s.wav').play()
		#time.sleep(2)	

def sound6(time6,time):
	if deftime(time6,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c2.wav').play()
		#time.sleep(2)	

def sound7(time7,time):
	if deftime(time7,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1.wav').play()
		#time.sleep(2)	

def sound8(time8,time):
	if deftime(time8,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1s.wav').play()
		#time.sleep(2)	

def sound9(time9,time):
	if deftime(time9,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/e1.wav').play()
		#time.sleep(2)	

def sound10(time10,time):
	if deftime(time10,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1.wav').play()
		#time.sleep(2)	

def sound11(time11,time):
	if deftime(time11,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1s.wav').play()
		#time.sleep(2)	

def sound12(time12,time):
	if deftime(time12,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1.wav').play()
		#time.sleep(2)	

def sound13(time13,time):
	if deftime(time13,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1s.wav').play()
		#time.sleep(2)	

def sound14(time14,time):
	if deftime(time14,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
		#time.sleep(2)	

def deftime(t1,t2):
	return t2-t1

cap = cv2.VideoCapture(1)
# vs = WebcamVideoStream(src=1).start()
k = True
key_threshold = 900
ret, t0 = cap.read()
ret, t1 = cap.read()
# t0 = vs.read()
# t1 = vs.read()
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)

while True:
	t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
	diff = cv2.absdiff(t1, t0)
	ret,threshold_image = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	key1 = cv2.countNonZero(threshold_image[355:410,0:35])
	key2 = cv2.countNonZero(threshold_image[355:410,40:85])
	key3 = cv2.countNonZero(threshold_image[355:410,90:130])
	key4 = cv2.countNonZero(threshold_image[355:410,135:183])
	key5 = cv2.countNonZero(threshold_image[355:410,183:230])
	key6 = cv2.countNonZero(threshold_image[355:410,230:275])
	key7 = cv2.countNonZero(threshold_image[355:410,275:325])
	key8 = cv2.countNonZero(threshold_image[355:410,325:370])
	key9 = cv2.countNonZero(threshold_image[355:410,370:420])
	key10 = cv2.countNonZero(threshold_image[355:410,420:470])
	key11 = cv2.countNonZero(threshold_image[355:410,470:515])
	key12 = cv2.countNonZero(threshold_image[355:410,515:560])
	key13 = cv2.countNonZero(threshold_image[355:410,560:610])
	key14 = cv2.countNonZero(threshold_image[355:410,610:638])
	
	if k:
	 	if key1 > key_threshold:
	 		Thread(target=sound1(time1,time.time())).start()
	 		time1=time.time()

	 	if key2 > key_threshold:
	 		Thread(target=sound2(time2,time.time())).start()
	 		time2=time.time()

	 	if key3 > key_threshold:
	 		Thread(target=sound3(time3,time.time())).start()
	 		time3=time.time()

	 	if key4 > key_threshold:
	 		Thread(target=sound4(time4,time.time())).start()
	 		time4=time.time()

	 	if key5 > key_threshold:
	 		Thread(target=sound5(time5,time.time())).start()
	 		time5=time.time()

	 	if key6 > key_threshold:
	 		Thread(target=sound6(time6,time.time())).start()
	 		time6=time.time()

	 	if key7 > key_threshold:
	 		Thread(target=sound7(time7,time.time())).start()
	 		time7=time.time()

	 	if key8 > key_threshold:
	 		Thread(target=sound8(time8,time.time())).start()
	 		time8=time.time()

	 	if key9 > key_threshold:
	 		Thread(target=sound9(time9,time.time())).start()
	 		time9=time.time()

	 	if key10 > key_threshold:
	 		Thread(target=sound10(time10,time.time())).start()
	 		time10=time.time()

	 	if key11 > key_threshold:
	 		Thread(target=sound11(time11,time.time())).start()
	 		time11=time.time()

	 	if key12 > key_threshold:
	 		Thread(target=sound12(time12,time.time())).start()
	 		time12=time.time()

	 	if key13 > key_threshold:
	 		Thread(target=sound13(time13,time.time())).start()
	 		time13=time.time()

	 	if key14 > key_threshold:
	 		Thread(target=sound14(time14,time.time())).start()
	 		time14=time.time()

	k = not k
	cv2.imshow('Window', threshold_image)

	t0 = t1
	ret, t1 = cap.read()
	#t1 = vs.read()	
	#time.sleep(0.1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
#vs.stop()
