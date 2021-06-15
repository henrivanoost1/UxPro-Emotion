from flask import Flask, render_template, Response
from camera import VideoCamera
# from camera import length
import time
import subprocess
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
    # length_video=camera.get_length()
    # print(length_video)
    start_time=time.time()
    array_first_time=[]
    my_dict = {"emotion":[],"start_time":[],"end_time":[]}
    counter=0
    # camera.make_video()
    #jkk



    path_data="last_data"
    count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])+1

    test_data={}

    with open(os.path.join(path_data,"last_data"+str(count_json)+".json"),"w") as file:
        json.dump(test_data,file)


    
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
        # array_keys5=array_keys5.replace("'","")
        array_keys5= array_keys5.split(",")

        time_start= float(array_keys5[0])
        time_end=float(array_keys5[len(array_keys5)-1])

        time_calc=time_end-time_start

        # for i in range(len(array_keys5)):
        #     pass
        #     # print(array_keys5[i])

        array_values= to_python.values()
        array_values1= str(array_values)
        array_values2= array_values1.replace("([","")
        array_values3=array_values2.replace("])","")
        array_values4=array_values3.replace("dict_values","")
        array_values5=array_values4.replace("'","")
        # array_values5=array_values5.replace("'","")
        array_values5= array_values5.split(",")
        
        # print(array_values5)
        array_values_correction=[]
        array_keys_correction=[]

        # path_data="static/data"
        # count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])+1

        # test_data={"Emotions":[]}

        # with open(os.path.join(path_data,"data"+str(count_json)+".json"),"w") as file:
        #     json.dump(test_data,file,indent=4)  

        for i in range(len(array_values5)):
            if i==0:
                # new_time=array_keys5[i]-array_keys5[0]
                new_time=0
                new_time=time.strftime('%H:%M:%S', time.gmtime(new_time))

                new_emotion= array_values5[i]
                array_values_correction.append(new_emotion)
                array_keys_correction.append(new_time)
                
            if i>1:
                if array_values5[i]!=array_values5[i-1]:
                    new_time=float(array_keys5[i])-float(array_keys5[0])
                    new_time=time.strftime('%H:%M:%S', time.gmtime(new_time))
                    new_emotion= array_values5[i]
                    array_values_correction.append(new_emotion)
                    array_keys_correction.append(new_time)
                
                else:
                    pass
        full_data_json=[]

        path_data="static/data"
        count_json= len([name for name in os.listdir(path_data) if os.path.isfile(os.path.join(path_data, name))])+1

        

        # with open(os.path.join(path_data,"data"+str(count_json)+".json"),"w") as file:
        #     json.dump(full_data_json,file,indent=4) 

        list_moments=[] 

        for i in range(len(array_keys_correction)):
            # if i==0:
            #     test_data={"StartTime":str(start_time), "EndTime":str(end_time),"Emotion":str(emotion)}


            if i< (len(array_keys_correction)-1):
                print(i)
                start_time=array_keys_correction[i]
                end_time=array_keys_correction[i+1]
                emotion= array_values_correction[i]
                # test_data="{'StartTime':"+str(start_time)+", 'EndTime':"+str(end_time)+",'Emotion':"+str(emotion)+"},"
                # test_data={"StartTime":str(start_time), "EndTime":str(end_time),"Emotion":str(emotion)},

                test_data=dict(StartTime=str(start_time),EndTime=str(end_time),Emotion=str(emotion) )
                list_moments.append(test_data)

                # full_data_json=full_data_json+test_data

                # with open(os.path.join(path_data,"data"+str(count_json)+".json"),"r+") as file:
                #     file_data=json.load(file)
                #     file_data.update(test_data)
                #     file.seek(0)
                #     json.dump(test_data,file,indent=4)
            else:
                print(i)
                start_time=array_keys_correction[i]
                end_time=array_keys_correction[i]
                emotion= array_values_correction[i]
            
                # test_data={"StartTime":str(start_time), "EndTime":str(end_time),"Emotion":str(emotion)}
                test_data=dict(StartTime=str(start_time),EndTime=str(end_time),Emotion=str(emotion))
                list_moments.append(test_data)

                # full_data_json=full_data_json+test_data+end_data
            
        print(list_moments)

        with open(os.path.join(path_data,"data"+str(count_json)+".json"),"w") as file:
            json.dump(list_moments,file,indent=4)
        
        folder = 'last_data'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        # with open(os.path.join(path_data,"data"+str(count_json)+".json"),"w") as file:
        #     # file_data=json.load(file)
        #     # print(file_data)
        #     # file_data.update(list_moments)
        #     # file.seek(0)
        #     json.dump(list_moments,file,indent=4)
        
        

        

            


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
