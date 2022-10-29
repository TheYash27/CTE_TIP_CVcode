# sets up trackbars to ananlyze image in HSV colorspace
#shows trackbar mask, input and result
# see https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/ for more info on colorspace 
#esc to quit
#red typical H: 156-179, S:117-255 , V: 98-255
#green typical H: 40-85, S:255-255 , V: 19-255
#blue typical H: 100-127, S:107-255 , V: 152-255
#yellow typical H: 15-35, S:77-255 , V: 165-255

import cv2 #importing the Computer Vision library
import numpy as np #importing NumPy for writing Python functions seamlessly
from matplotlib import pyplot as plt # for visualizing the image(s)
 
def nothing(x):
    pass

#setparameters input /output file/display size

#The following code imports 1 image file, and exports 2 of them
filein = '/home/pi/Desktop/starpattern1.jpg'
#mask output
FILEOUT1 = '/home/pi/Desktop/result.png'
#result output
FILEOUT2 = '/home/pi/Desktop/mask.png'


#rsize parameter , smaller < 1
#resizes for display   .2 for 3280x2464, 1 for 640x480
rsize =.2

#read file in color
img = cv2.imread(filein, 1)

#establish initial range 
Hstart,Sstart,Vstart = 0,0,0
Hend,Send,Vend = 179,255,255

#convert into HSV colorspace (It's jus like RGB - hue, saturation and value (which could also be seen as magnitude / fraction)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#The following code defines within what hsv values we are looking for - sorta like a range of detection
lower_range = np.array([Hstart,Sstart,Vstart], dtype=np.uint8)
upper_range = np.array([Hend,Send,Vend], dtype=np.uint8)

#initializing the mask, which is basically used to amplify our desired range of hsv values (that we specified earlier) / suppress the unwanted colours from our image
mask = cv2.inRange(hsv, lower_range, upper_range)

maskr = cv2.resize(mask,None,fx=rsize, fy=rsize, interpolation = cv2.INTER_CUBIC)
imgr = cv2.resize(img,None,fx=rsize, fy=rsize, interpolation = cv2.INTER_CUBIC)

#displaying the masked and orig. image in 2 windows 
cv2.imshow('mask',maskr)
cv2.imshow('image', imgr)
 
cv2.createTrackbar('Hstart','mask',0,179,nothing)
cv2.createTrackbar('Hend','mask',0,179,nothing)

cv2.createTrackbar('Sstart','mask',0,255,nothing)
cv2.createTrackbar('Send','mask',0,255,nothing)

cv2.createTrackbar('Vstart','mask',0,255,nothing)
cv2.createTrackbar('Vend','mask',0,255,nothing)

#The following inf. while loop basically keeps re - factoring the orig. img. based on the range of hsv values present in the 'mask' img.
#We do this by utilizing a HSV color trackbar (hence, the name of the file)
while(1):

    maskr = cv2.resize(mask,None,fx=rsize, fy=rsize, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('mask',maskr)

    imgr = cv2.resize(img,None,fx=rsize, fy=rsize, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('image', imgr)
     
    Hstart = cv2.getTrackbarPos('Hstart', 'mask')
    Hend = cv2.getTrackbarPos('Hend', 'mask')

    Sstart = cv2.getTrackbarPos('Sstart', 'mask')
    Send = cv2.getTrackbarPos('Send', 'mask')
    
    Vstart = cv2.getTrackbarPos('Vstart', 'mask')
    Vend = cv2.getTrackbarPos('Vend', 'mask')

    lower_range = np.array([Hstart,Sstart,Vstart], dtype=np.uint8)
    upper_range = np.array([Hend,Send,Vend], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_range, upper_range)

    result = cv2.bitwise_and(img,img,mask = mask)
    imgr = cv2.resize(result,None,fx=rsize, fy=rsize, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('result',imgr)
 
 
    # press escape to exit 
    k = cv2.waitKey(37)
    if k == 27:
        break

#exporting the final result img. and the mask img.
cv2.imwrite(FILEOUT1,result)
cv2.imwrite(FILEOUT2,mask)

#cleaning up the mess before moving fwd.
cv2.destroyAllWindows()


"""


img = cv2.blur(img_noblur, (7,7))

#https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
canny_edge = cv2.Canny(img, 0, 0)

#creating and displaying the img.
imgr = cv2.resize(img,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('image', imgr)

#creating and displaying the canny edges (basically, outline)
res = cv2.resize(canny_edge,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('canny_edge', canny_edge)
 
cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
cv2.createTrackbar('max_value','canny_edge',0,500,nothing)

#doing with the outlines of the img., what we 1st did with the mask img.  
while(1):

    imgr = cv2.resize(img,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('image', imgr)
    
    #cv2.imshow('image', img)

    res = cv2.resize(canny_edge,None,fx=.2, fy=.2, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('canny_edge', res)
     
    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
 
    canny_edge = cv2.Canny(img, min_value, max_value)
     
    k = cv2.waitKey(37)
    if k == 27:
        break

 """
