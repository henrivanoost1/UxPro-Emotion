import cv2
from model import FacialExpressionModel
import numpy as np
from moviepy.editor import VideoFileClip
import os
import time
import json


facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_PLAIN
timet= time
jsontest= json

class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture('videos/presidential_debate.mp4')
        # self.video = cv2.VideoCapture('videos/facial_exp.mkv')
        # self.video = cv2.VideoCapture('videos/test.mp4')

        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('videos/Video1.mp4')

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        counter=0
        counter=counter+1
        path= "images"
        
        
        

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            time= timet.time()
            cv2.putText(fr, pred, (x+(w//3), y-5), font, 5, (0, 0, 255), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
            y={str(time):str(pred)}
            with open("test1.json",'r+') as file:
            # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_dat3a with file_data
                file_data.update(y)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
            


            

        # _, jpeg = cv2.imencode('.jpg', fr)

        # cv2.imwrite(os.path.join(path, "img"+str(counter)+".jpg"),fr)
        return fr
    
    def get_length(self):
        clip = VideoFileClip("videos/test.mp4")
        return clip.duration

    def make_video(self):
        cap= self.video
        i=0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            cv2.imwrite('img'+str(i)+'.jpg',frame)
            
            i+=1
        
        cap.release()
        cv2.destroyAllWindows()