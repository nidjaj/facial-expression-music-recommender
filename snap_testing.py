#!/usr/bin/python3

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cv2
# import sys

# parameters for loading data and images
detection_model_path = 'cascade/haarcascade_frontalface_alt.xml'
emotion_model_path = 'models/model.hdf5'

# loading models
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["Angry", "Disgust", "Scared", "Happy", "Sad", "Surprised", "Neutral"]

#f = open("/var/www/html/imageid.txt","r")
#imageid=f.read()
#print(imageid)
#imgpath = "/html/"+imageid
#print(imgpath)

frame = cv2.imread("image.jpeg")
orig_frame = frame
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_detection.detectMultiScale(frame, scaleFactor=1.4, minNeighbors=5, minSize=(30, 30),
                                        flags=cv2.CASCADE_SCALE_IMAGE)
if len(faces) != 0:
    faces = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
    (fX, fY, fW, fH) = faces
    roi = frame[fY:fY + fH, fX:fX + fW]
    roi = cv2.resize(roi, (48, 48))
    roi = roi.astype("float") / 255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    preds = emotion_classifier.predict(roi)[0]
    emotion_probability = np.max(preds)
    label = EMOTIONS[preds.argmax()]
    #print('Person seams to be: ' + label)
    cv2.putText(orig_frame, label, (fX, fY - 10), cv2.FONT_HERSHEY_DUPLEX, 0.45, (150, 50, 180), 2)
    cv2.rectangle(orig_frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)
    fp = open("label.txt","w")
    fp.write(label)
    fp.close()




#cv2.imshow('FER', orig_frame)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
print("<meta http-equiv='refresh' content='0;url=/html/sentisnap.html'>")

