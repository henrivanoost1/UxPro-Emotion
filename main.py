from flask import Flask, render_template, Response
from camera import VideoCamera
# from camera import length
import time
import subprocess
import cv2
import os

start_time=""
end_time=""

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    # length_video=camera.get_length()
    # print(length_video)
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

        
        # array_first_time.append(end_time)
        # end_time_correction=array_first_time[0]
        # correction=end_time_correction-start_time
        # time_duration= end_time-start_time
        # final_time= time_duration-correction

        # convert_time= array_first_time[len(array_first_time)-1] - array_first_time[0]
        
        # print(f"tijd: {time_duration}")
        # print(f"final time: {final_time}")
        # print(f"tijd voor converting: {convert_time}")
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video')
def video():
    example_embed='<a href="www.google.be">This string is from python</a>'
    return render_template('video.html', embed=example_embed)

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

    # for filename in glob.glob(f'images/*[0-{num_files}].jpg'):
    #     img = cv2.imread(filename)
    #     array_filename.append(filename)
    
    #     height, width, layers = img.shape
    #     size = (width,height)
    #     img_array.append(img)

    DIR="static/videos"
    


    count= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])+1

    
    out = cv2.VideoWriter(os.path.join("static/videos",f'project{count}.webm'),cv2.VideoWriter_fourcc(*'VP90'), 5.844723165033935, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
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
