# Reading, displaying and saving images
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\hp\Downloads\images (1).jpg")
cv2.imshow("Image", img)

#Resizing images
height= 700
width = 700
resizing = (height,width)
resized = cv2.resize(img,resizing)
cv2.imshow("resized image",resized)

# Flipping images (horizontal, vertical, both)
flip_vartical=cv2.flip(img,0)
cv2.imshow("flipped vertical image",flip_vartical)

flip_horizontal= cv2.flip(img,1)
cv2.imshow("flipped horizontal image",flip_horizontal)

# Drawing shapes lines adding text on images
img2 = cv2.imread(r"C:\Users\hp\Downloads\images (1).jpg",cv2.IMREAD_COLOR)
# draw line
cv2.line(img2,(0,0), (150,150),(255,34,89),3)
# draw rectangle
cv2.rectangle(img2,(200,150),(250,300),(0.255,0),3)
# draw circle
cv2.circle(img2,(300,75),70,(255,0,255),3)
# text on image
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img2,'Hello!',(10,500),font, 3,(200,255,255),8,cv2.LINE_AA)
cv2.imshow("diagram image",img2)

#Image translation(shifting) using warpAffine
column = img.shape[1]
row = img.shape[0]
s = np.float32([ [1, 0, 150],[0, 1, 70]])
shifted = cv2.warpAffine(img, s, (column, row))
cv2.imshow("shifted image",shifted)

#Image rotation using getRotationMatrix2D and warpAffine
center = (column/2,row/2)
angle = 90
r1 = cv2.getRotationMatrix2D(center,angle,1)
rotation = cv2.warpAffine(img,r1,(column,row))
cv2.imshow("rotated image",rotation)

# Thresholding (Binary threshold)
threshold_value = 200
_,binary_threshold = cv2.threshold(img,threshold_value,255, cv2.THRESH_BINARY)
cv2.imshow("binary threshold",binary_threshold)

#Blurring images using Gaussian Blur and Median Blur
resize = cv2.resize(img, (640,640))
kernal_size = (7,7)
sigmax  = 0
sigmay  = 0
blur = cv2.GaussianBlur(resize,kernal_size,sigmax)
cv2.imshow('Input', resize)
cv2.imshow('Output', blur)

#Morphological operations (Tophat, Blackhat)
width = 600
heigh = 850
dim =(width,height)
resized = cv2.resize(img,dim)

kernel = np.ones((5,5),dtype='uint8')
tophat =  cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("Tophat",tophat)
cv2.imshow("Blackhat",blackhat)

# Edge detection using Canny
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny Edge Detection", edges)

#Reading and writing video files
# Reading video file
video = cv2.VideoCapture(
    r"C:\Users\hp\Downloads\857183-hd_1920_1080_25fps.mp4"
)

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(
    'Output.mp4',
    fourcc,
    25.0,
    (width, height))

while video.isOpened():
    ret, frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(10) & 0xFF == ord('s'):
            break
    else:
        break
video.release()
output.release()

# Capturing live video from webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    if not ret:
        print("Unable to access webcam")
        break

    # Show live video
    cv2.imshow("Webcam", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
video.release()

cv2.waitKey(0)
cv2.destroyAllWindows()