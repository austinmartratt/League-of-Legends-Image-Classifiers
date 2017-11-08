#Austin Martratt
#11/08/2017
#simple script to output frame using openCV from selected area of the screen
#then save the frame to folder path with name as unix time stamp
#This is a useful way to collect a lot of images for training the neural net
#Currently exports ~10 frames per second to folder path
import sys
import numpy as np
from PIL import ImageGrab
import cv2
import time
from numpy import ones,vstack
from numpy.linalg import lstsq
import os
import PIL.Image

counter =0
last_time = time.time()
while True:


    screen =  np.array(ImageGrab.grab(bbox=(950,275,1125,475))) #grab the image from computer screen at coordinates (x, y, xx, yy) , x,y = top left , xx,yy = bottom right
    fps = (1 / (time.time()-last_time))
    if counter == 10:
        print('FPS:' + str(fps))
        counter = 0
    else:
        counter += 1
    last_time = time.time()
    timeu = format(time.time()-last_time)
    #PIL image from ImageGrab needs to be fixed to work with OpenCV representation
    image = np.array(screen) # Convert PIL Image to numpy/OpenCV image representation
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # convert current image from RGB to BGR
    cv2.imshow('window', image)
    path = 'C:/Users/Austin/Documents/GitHub/League-of-Legends-Image-Classifiers/Data/TestImages'
    imagename = str(time.time()) + ".jpg"
    cv2.imwrite(os.path.join(path , imagename ), image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
