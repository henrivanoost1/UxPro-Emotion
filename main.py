from flask import Flask, render_template, Response
from camera import VideoCamera
# from camera import length
import time
import subprocess
import cv2
import os

start_time=""
end_time=""

app = Flask(__name__, static_folder='videos')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    length_video=camera.get_length()
    print(length_video)
    start_time=time.time()
    array_first_time=[]
    my_dict = {"emotion":[],"start_time":[],"end_time":[]}
    counter=0
    # camera.make_video()
    
    while True:
        
        counter=counter+1
        path= "images"
        
        frame = camera.get_frame()
        end_time=time.time()

        _, jpeg = cv2.imencode('.jpg', frame)


        cv2.imwrite(os.path.join(path, "img"+str(counter)+".jpg"),frame)
        frame= jpeg.tobytes()

        
        array_first_time.append(end_time)
        end_time_correction=array_first_time[0]
        correction=end_time_correction-start_time
        time_duration= end_time-start_time
        final_time= time_duration-correction

        convert_time= array_first_time[len(array_first_time)-1] - array_first_time[0]
        
        print(f"tijd: {time_duration}")
        print(f"final time: {final_time}")
        print(f"tijd voor converting: {convert_time}")
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video')
def video():
    return render_template('video.html')

# @app.route('/videoframe')
# def video():
#     return render_template('video.html')



@app.route('/video_feed_test')
def video_feed_test():
    

    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
