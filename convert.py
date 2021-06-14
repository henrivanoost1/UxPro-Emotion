import cv2
import numpy as np
import glob
import os.path
 
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
 
 
 
out = cv2.VideoWriter('project1.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 8.071284370761148, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print(array_filename)