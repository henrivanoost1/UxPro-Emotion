from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import cv2
import os, shutil
import json

start_time=""
end_time=""

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    counter=0
    path_data="last_data"
    count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])+1
    test_data={}
    with open(os.path.join(path_data,"last_data"+str(count_json)+".json"),"w") as file:
        json.dump(test_data,file)

    while True:
        
        counter=counter+1
        path= "images"
        
        frame = camera.get_frame()
        _, jpeg = cv2.imencode('.jpg', frame)

        cv2.imwrite(os.path.join(path, "img"+str(counter)+".jpg"),frame)
        frame= jpeg.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video')
def video():  
    return render_template('video.html')

@app.route('/videosave')
def videosave():
    img_array = []
    array_filename=[]
    path = 'images'
    num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

    for i in range(num_files):
        i=i+1
        filename=f"images/img{i}.jpg"
        img = cv2.imread(filename)
        array_filename.append(filename)
    
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    DIR="static/videos"
    count= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])+1

    out = cv2.VideoWriter(os.path.join("static/videos",f'project{count}.webm'),cv2.VideoWriter_fourcc(*'VP90'), 5.844723165033935, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    folder = 'images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    path_data="last_data"
    count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])
    with open(f"last_data/last_data{count_json}.json", 'r+') as file:
        to_python= json.loads(file.read())

        array_keys= to_python.keys()
        array_keys1= str(array_keys)
        array_keys2= array_keys1.replace("([","")
        array_keys3=array_keys2.replace("])","")
        array_keys4=array_keys3.replace("dict_keys","")
        array_keys5=array_keys4.replace("'","")
        array_keys5= array_keys5.split(",")

        array_values= to_python.values()
        array_values1= str(array_values)
        array_values2= array_values1.replace("([","")
        array_values3=array_values2.replace("])","")
        array_values4=array_values3.replace("dict_values","")
        array_values5=array_values4.replace("'","")
        array_values5= array_values5.split(",")
        
        array_values_correction=[]
        array_keys_correction=[]

        for i in range(len(array_values5)):
            if i==0:
                new_time=0
                # new_time=time.strftime('%H:%M:%S', time.gmtime(new_time))
                new_emotion= array_values5[i]
                array_values_correction.append(new_emotion)
                array_keys_correction.append(new_time)
                
            if i>1:
                if array_values5[i]!=array_values5[i-1]:
                    new_time=float(array_keys5[i])-float(array_keys5[0])
                    # new_time=time.strftime('%H:%M:%S', time.gmtime(new_time))
                    new_emotion= array_values5[i]
                    array_values_correction.append(new_emotion)
                    array_keys_correction.append(new_time)
                
                else:
                    pass
        path_data="static/data"
        count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])+1

        list_moments=[] 
        for i in range(len(array_keys_correction)):
            if i< (len(array_keys_correction)-1):
                print(i)
                start_time=array_keys_correction[i]
                end_time=array_keys_correction[i+1]
                emotion= array_values_correction[i]

                test_data=dict(StartTime=str(start_time),EndTime=str(end_time),Emotion=str(emotion) )
                list_moments.append(test_data)
            else:
                print(i)
                start_time=array_keys_correction[i]
                end_time=array_keys_correction[i]
                emotion= array_values_correction[i]            
                test_data=dict(StartTime=str(start_time),EndTime=str(end_time),Emotion=str(emotion))
                list_moments.append(test_data)
            
        print(list_moments)

        with open(os.path.join(path_data,"data"+str(count_json)+".json"),"w") as file:
            json.dump(list_moments,file,indent=4)

        with open(os.path.join("static/js","aantal.json"),"w") as file:
            path_data="static/data"
            count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])
            text=[count_json]
            json.dump(text,file)
        
    return render_template('video.html')


@app.route('/video_feed_test')
def video_feed_test():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
