import cv2
import numpy as np
from threading import Thread
from playsound import playsound

cap = cv2.VideoCapture(1)
k = True
key_threshold = 1200
ret, t0 = cap.read()
ret, t1 = cap.read()
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
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key2 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key3 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key4 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key5 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key6 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key7 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key8 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key9 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key10 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key11 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key12 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key13 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break

		if key14 > key_threshold:
			Thread(target=playsound('/home/ajinkya/Downloads/wav-piano-sound-master/wav/a1.wav')).start()
			break
			
	k = not k
	cv2.imshow('Window', threshold_image)

	t0 = t1
	ret, t1 = cap.read()	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
