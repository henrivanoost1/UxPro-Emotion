from flask import Flask, render_template, Response
# from camera import VideoCamera
import time
import subprocess
import cv2
import os

start_time=""
end_time=""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    pass


    

@app.route('/video_feed_test')
def video_feed_test():
    pass
    

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
