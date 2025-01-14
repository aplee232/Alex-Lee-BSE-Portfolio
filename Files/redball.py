# import the necessary packages
from picamera.array import PiRGBArray     #As there is a resolution problem in raspberry pi, will not be able to capture frames by VideoCapture
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2
import cv2 as cv
import numpy as np

#hardware work
GPIO.setmode(GPIO.BCM)

TRIG = 23      #Front ultrasonic sensor
ECHO = 22

MOTOR1B = 19  #Left Motor pins 1B=2, 1E=1 on H-bridge
MOTOR1E = 26

MOTOR2B = 13  #Right Motor pins 2B=4, 2E=3
MOTOR2E = 6

#LED_PIN = 13  #If it finds the ball, then it will light up the led

# Set pins as output and input
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
#GPIO.setup(LED_PIN,GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(TRIG, False)

# Allow module to settle
def sonar(TRIG,ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    return distance

GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR1E, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)
GPIO.setup(MOTOR2E, GPIO.OUT)

def forward():
      GPIO.output(MOTOR1B, True)
      GPIO.output(MOTOR1E, False)
      GPIO.output(MOTOR2B, True)
      GPIO.output(MOTOR2E, False)

     
def reverse():
      GPIO.output(MOTOR1B, False)
      GPIO.output(MOTOR1E, True)
      GPIO.output(MOTOR2B, False)
      GPIO.output(MOTOR2E, True)

     
def turnright():
      GPIO.output(MOTOR1B, False)
      GPIO.output(MOTOR1E, True)
      GPIO.output(MOTOR2B, True)
      GPIO.output(MOTOR2E, False)

     
def turnleft():
      GPIO.output(MOTOR1B, True)
      GPIO.output(MOTOR1E, False)
      GPIO.output(MOTOR2B, False)
      GPIO.output(MOTOR2E, True)
   

def stop():
      GPIO.output(MOTOR1E, False)
      GPIO.output(MOTOR1B, False)
      GPIO.output(MOTOR2E, False)
      GPIO.output(MOTOR2B, False)
   
     
#Image analysis work
def segment_colour(frame):    #returns only the red colors in the frame
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([160, 160,10]), np.array([190,255,255]))
    ycr_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    mask_2=cv2.inRange(ycr_roi, np.array((0.,165.,0.)), np.array((255.,255.,255.)))

    mask = mask_1 | mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)      #Eroding
    mask=cv2.dilate(mask,kern_dilate)     #Dilating
    #cv2.imshow('mask',mask)
    return mask

def find_blob(blob): #returns the red colored circle
    largest_contour=0
    cont_index=0
    contours, hierarchy = cv2.findContours(blob, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for idx, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area >largest_contour) :
            largest_contour=area
            cont_index=idx
                              
    r=(0,0,1,1)
    if len(contours) > 0:
        r = cv2.boundingRect(contours[cont_index])
       
    return r,largest_contour

def target_hist(frame):
    hsv_img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    hist=cv2.calcHist([hsv_img],[0],None,[50],[0,255])
    return hist

#CAMERA CAPTURE
#initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (160, 128)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(160, 128))

# allow the camera to warmup
time.sleep(0.001)
 
# capture frames from the camera
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      #grab the raw NumPy array representing the image, then initialize the timestamp and occupied/unoccupied text
      frame = image.array
      frame=cv2.flip(frame,1)
      global centre_x
      global centre_y
      centre_x=0.
      centre_y=0.
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      mask_red = segment_colour(frame)      #masking red the frame
      loct,area = find_blob(mask_red)
      x,y,w,h = loct
     
      #distance coming from front ultrasonic sensor
      distanceC = sonar(TRIG,ECHO)
             
      if (w*h) < 10:
            found=0
      else:
            found=1
            simg2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
            centre_x=x+((w)/2)
            centre_y=y+((h)/2)
            cv2.circle(frame,(int(centre_x),int(centre_y)),3,(0,110,255),-1)
            centre_x-=80
            centre_y=6--centre_y
            print (centre_x, centre_y)
      initial=400
      flag=0
      #GPIO.output(LED_PIN,GPIO.LOW)
      if(found==0):
            #if the ball is not found and the last time it sees ball in which direction, it will start to rotate in that direction
            if flag==0:
                  turnright()
                  time.sleep(0.05)
            else:
                  turnleft()
                  time.sleep(0.05)
            stop()
            time.sleep(0.0125)
     
      elif(found==1):
            print("distanceC = ", distanceC)
            print("area = ", area)
            if(area<initial):
                  if(distanceC<10):                        #otherwise it moves forward
                        forward()
                        time.sleep(0.00625)
            elif(area>=initial):
                  initial2=6700
                  if(area<initial2):
                        if(distanceC>10):
                              #it brings coordinates of ball to center of camera's imaginary axis.
                              if(centre_x<=-20 or centre_x>=20):
                                    if(centre_x<0):
                                          flag=0
                                          turnright()
                                          time.sleep(0.1)
                                    elif(centre_x>0):
                                          flag=1
                                          turnleft()
                                          time.sleep(0.1)
                              forward()
                              time.sleep(0.1)
                              stop()
                              time.sleep(0.00025)
                        else:
                              stop()
                              time.sleep(0.01)

                  else:
                        #if it founds the ball and it is too close it lights up the led.
                        #GPIO.output(LED_PIN,GPIO.HIGH)
                        time.sleep(0.1)
                        stop()
                        time.sleep(0.1)
      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)  # clear the stream in preparation for the next frame
         
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break

GPIO.cleanup() #free all the GPIO pins
