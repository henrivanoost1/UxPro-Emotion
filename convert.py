import cv2
import numpy as np
import glob
import os.path
import os
 
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
