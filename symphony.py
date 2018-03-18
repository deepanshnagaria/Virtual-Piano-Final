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
timed1=time.time()
timed2=time.time()
timed3=time.time()
timed4=time.time()
timed5=time.time()
timed6=time.time()
timed7=time.time()
timed8=time.time()

def sound1(time1,time):
	if deftime(time1,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
		#time.sleep(0.1)	

def sound2(time2,time):
	if deftime(time2,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1.wav').play()
		#time.sleep(2)	

def sound3(time3,time):
	if deftime(time3,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1.wav').play()
		#time.sleep(2)	

def sound4(time4,time):
	if deftime(time4,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/e1.wav').play()
		#time.sleep(2)	

def sound5(time5,time):
	if deftime(time5,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1.wav').play()
		#time.sleep(2)	

def sound6(time6,time):
	if deftime(time6,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1.wav').play()
		#time.sleep(2)	

def sound7(time7,time):
	if deftime(time7,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c2.wav').play()
		#time.sleep(2)	

def sound8(time8,time):
	if deftime(time8,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/b1.wav').play()
		#time.sleep(2)	

def sound9(time9,time):
	if deftime(time9,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav').play()
		#time.sleep(2)	

def sound10(time10,time):
	if deftime(time10,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/g1.wav').play()
		#time.sleep(2)	

def sound11(time11,time):
	if deftime(time11,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/f1.wav').play()
		#time.sleep(2)	

def sound12(time12,time):
	if deftime(time12,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/e1.wav').play()
		#time.sleep(2)	

def sound13(time13,time):
	if deftime(time13,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/d1.wav').play()
		#time.sleep(2)	

def sound14(time14,time):
	if deftime(time14,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/c1.wav').play()
		#time.sleep(2)	

def drum1(timed1,time):
	if deftime(timed1,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/thaal.ogg').play()
		#time.sleep(2)	

def drum2(timed2,time):
	if deftime(timed2,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/motha.ogg').play()
		#time.sleep(2)	

def drum3(timed3,time):
	if deftime(timed3,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/drum1.ogg').play()
		#time.sleep(2)	

def drum4(timed4,time):
	if deftime(timed4,time) > delay:
		pygame.mixer.Sound('/home/ajinkya/Downloads/motha.ogg').play()
		#time.sleep(2)

def arcreactersound(timed5,time):
	if deftime(timed5,time) > 10:
		pygame.mixer.Sound('/home/ajinkya/Downloads/dil.ogg').play()
		#time.sleep(2)

def hammersound(timed6,time):
	if deftime(timed6,time) > 10:
		pygame.mixer.Sound('/home/ajinkya/Downloads/albatroz-[AudioTrimmer.com].ogg').play()
		#time.sleep(2)

def dhaalsound(timed7,time):
	if deftime(timed7,time) > 10:
		pygame.mixer.Sound('/home/ajinkya/Downloads/zing.ogg').play()
		#time.sleep(2)

def spidersound(timed8,time):
	if deftime(timed8,time) > 10:
		pygame.mixer.Sound('/home/ajinkya/Downloads/dil.ogg').play()
		#time.sleep(2)

def deftime(t1,t2):
	return t2-t1

cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
# vs = WebcamVideoStream(src=1).start()
k = True
key_threshold = 750
ret, t0 = cap.read()
ret, t1 = cap.read()
ret, tt0 = cap2.read()
ret, tt1 = cap2.read()

# t0 = vs.read()
# t1 = vs.read()
image1 = t0
image2 = tt0
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
tt0 = cv2.cvtColor(tt0, cv2.COLOR_BGR2GRAY)

while True:
	t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
	tt1 = cv2.cvtColor(tt1, cv2.COLOR_BGR2GRAY)
	diff = cv2.absdiff(t1, t0)
	diff2 = cv2.absdiff(tt1, tt0)
	ret,threshold_image = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	ret,threshold_image2 = cv2.threshold(diff2, 25, 255, cv2.THRESH_BINARY)
	key1 = cv2.countNonZero(threshold_image[355:410,0:25])
	key2 = cv2.countNonZero(threshold_image[355:410,30:67])
	key3 = cv2.countNonZero(threshold_image[355:410,77:120])
	key4 = cv2.countNonZero(threshold_image[355:410,180:170])
	key5 = cv2.countNonZero(threshold_image[355:410,180:220])
	key6 = cv2.countNonZero(threshold_image[355:410,230:270])
	key7 = cv2.countNonZero(threshold_image[355:410,280:320])
	key8 = cv2.countNonZero(threshold_image[355:410,330:370])
	key9 = cv2.countNonZero(threshold_image[355:410,377:418])
	key10 = cv2.countNonZero(threshold_image[355:410,425:465])
	key11 = cv2.countNonZero(threshold_image[355:410,477:518])
	key12 = cv2.countNonZero(threshold_image[355:410,525:562])
	key13 = cv2.countNonZero(threshold_image[355:410,575:610])
	key14 = cv2.countNonZero(threshold_image[355:410,620:640])
	cymbal = cv2.countNonZero(threshold_image2[130:260,30:180])
	big = cv2.countNonZero(threshold_image2[200:260,315:375])
	medium = cv2.countNonZero(threshold_image2[5:45,415:470])
	small = cv2.countNonZero(threshold_image2[65:100,205:255])
	arcreacter = cv2.countNonZero(threshold_image2[320:360,455:505])
	hammer = cv2.countNonZero(threshold_image2[240:280,500:545])
	dhaal = cv2.countNonZero(threshold_image2[155:185,480:525])
	spider = cv2.countNonZero(threshold_image2[105:135,435:465])

	
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

	 	if key14 > 550:
	 		Thread(target=sound14(time14,time.time())).start()
	 		time14=time.time()

		if cymbal>1000:
			Thread(target = drum1(timed1,time.time())).start()
			time1=time.time()
			#playsound('/home/ajinkya/Downloads/191490__alteration__cymbal.wav')
		if big>100:
			Thread(target = drum2(timed2,time.time())).start()

		if medium>100:
			Thread(target = drum3(timed3,time.time())).start()

		if small>100:
			Thread(target = drum4(timed4,time.time())).start()

		if arcreacter>100:
		 	Thread(target = arcreactersound(timed5,time.time())).start()

		if hammer>100:
		 	Thread(target = hammersound(timed6,time.time())).start()

		if dhaal>100:
		  	Thread(target = dhaalsound(timed7,time.time())).start()

		# if spider>100:
		#  	Thread(target = spidersound(timed8,time.time())).start()



	k = not k
	cv2.imshow('Window', t0)
	cv2.imshow('Window2', tt0)

	t0 = t1
	tt0 = tt1
	ret, t1 = cap.read()
	ret, tt1 = cap2.read()
	#t1 = vs.read()	
	#time.sleep(0.1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
#vs.stop()
