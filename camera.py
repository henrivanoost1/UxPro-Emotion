
import cv2
from numpy.core.numeric import full
from numpy.core.records import array
from model import FacialExpressionModel
import numpy as np
from moviepy.editor import VideoFileClip
import os
import time
import json
import math

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
        img = cv2.imread('emotions\\empty.png')
        
        

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            time= timet.time()
            cv2.putText(fr, pred, (x+(w//3), y-5), font, 5, (0, 0, 255), 2)
            
            
            if pred == 'Angry':
                img = cv2.imread('emotions\\angry.png')
            elif pred == 'Disgust':
                img = cv2.imread('emotions\\disgusted.png')
            elif pred == 'Happy':
                img = cv2.imread('emotions\\happy.png')
            elif pred == 'Neutral':
                img = cv2.imread('emotions\\neutral.png')
            elif pred == 'Sad':
                img = cv2.imread('emotions\\sad.png')
            



            percentage = model.percentage_emotion(roi[np.newaxis, :, :, np.newaxis])
            

            percentage = str(percentage)
            percentage = percentage.replace("[[", "")
            percentage = percentage.replace("]]", "")
        	

            list_percentages = percentage.split(" ")


            list_emotions = ["Angry", "Disgust", "Happy", "Neutral","Sad"]
            counter_position = 20
            counter_percentage = 0


            for i in list_percentages:
                if i == '' or i == ' ':
                    list_percentages.remove(i)


            substring = "e-"
            list_emotions_percentages = []

            for i in list_emotions:
                if substring in list_percentages[counter_percentage]:
                    full_percentage = list_percentages[counter_percentage]
                    percentages = full_percentage.split(substring)

                    grondtal = percentages[0]
                    macht = percentages[1]

                    percentage = float(grondtal) * (10 ** (float(macht) * -1))
                    percentage = percentage * 100
                    list_emotions_percentages.append(round(percentage, 4))

                else:
                    full_percentage = list_percentages[counter_percentage]
                    if full_percentage != "":
                        full_percentage = float(full_percentage)
                        percentage = full_percentage * 100
                        percentage = percentage               


                
                if len(list_emotions_percentages) != 0:
                    cv2.putText(fr, (i + ": " + str(list_emotions_percentages[counter_percentage])), (10,counter_position), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)

                counter_position += 30
                counter_percentage += 1

                

            
            path_data="last_data"
            count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])
            
        



            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
            y={str(time):str(pred)}
            with open(f"last_data/last_data{count_json}.json",'r+') as file:
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
        try:
            img_height, img_width, _ = img.shape
            x = 515
            y = 5
            fr[ y:y+img_height , x:x+img_width ] = img
        except AttributeError:
            print("shape not found")
            #code to move to next frame
            
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