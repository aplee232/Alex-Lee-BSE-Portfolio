# Ball Tracking Robot
This ball tracking robot does exactly as its name indicates, it tracks and follows a ball. This robot uses a Raspberry Pi and PiCamera for computer vision in order to find and track an object of a fixed color. It then uses an ultrasonic sensor and DC motors to first find where the ball is, then follow it.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Alex L. | Sequoia High School | Mechanical Engineering | Incoming Sophomore

# Modification: Robot Arm
My modification to my ball tracking robot is a robot arm. This kit by Cokoino is a a 4-axis robotic arm, propgrammed using an Arduino nano, moves using servo motors and controlled using a joystick controller. This was one of the easiest milestones/parts of this project because pretty much the entire kit worked when first assembled; it required significantly less troubleshooting compared to the other three milestones. One thing I needed to change from the original kit was the battery pack. This was because we did not have the two 18650 batteries that would fit into the original battery pack. I replaced it with a AA pack with 5 slots because the AA batteries supply much less voltage than the 18650s. 

One challenged I faced was the limited amount of time. I originally intended to have the claw push or pick up the ball, however there was no where on the robot where it could do that with this configuration, not to mention the claw which is too small to pick up the ball. With more time, I could have rewired everything in a way where the arm would fit properly, or CAD and 3D printed something to hold the claw or components. I also could have printed some kind of attachment to extend the actual claw so that it can fit around the ball.

Through this modification, I learned more about servo motors. I learned that servo motors can turn 180° (90° in either direction), and they are controlled by sending pulse width modulation (PWM). The amount of PWM in relation to the degree the servo moves varies between motors, however PWM and degrees turned has a high correlation in a positive linear relationship. The “neutral” position of a servo motors is at 90°, where the motor has equal potential to turn in either direction. They move the robot arm through teeth like gears which spin against another set of teeth on the arm, spinning it.
<br>  
# Final Milestone: Ultrasonic Sensor and DC Motors
<iframe width="560" height="315" src="https://www.youtube.com/embed/uMDJSQJW4MU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
My third milestone was getting the robot to actually track the red ball. It does this by communicating with an ultrasonic sensor, which in combination with the PiCamera, is able to find the location of the ball. The ultrasonic sensor has two transducers, one transmitter and one receiver/ One sends out an ultrasonic pulse which bounces off objects, returning back to the sensor. The sensor is coded to measure the time it takes for this “echo” to return, calculating distance with a basic Distance=Speed*Time equation, Distance=(pulse duration)*17150. The number, 17150, is the speed of sound at sea level (34300cm/s) divided by two because the distance is doubled (when the pulse is sent out and when it is reflected back). In combination with the code from the PiCamera, the ultrasonic sensor only detects the red ball, reporting values for its distance from the sensor. 

The second part of this milestone was the DC motors. Each motor requires 6V, however the base robot only comes with one battery pack which has only 6V. Since the motors are in series, the circuit requires a total of 12V, this forced me to add a second 6V battery pack which was connected in series.   I also connected the H-bridge, a device used to control speed and direction for multiple motors, to one of the ground pins on the Raspberry Pi, allowing the Pi to communicate with the H-bridge, telling the motors when to turn on. The batteries and motors are also connected to the H-bridge through the three ports that are on three sides of the H-bridge. There are six pins on an H-bridge, ENA, IN1, IN2, IN3, IN4 and ENB. The EN pins control speed while the IN pins control direction for their corresponding motors. 

The main problem I faced during this milestone was the inaccuracy of the original build guide. This was true in both the physical build as well as the code. For me, the schematic shown in the original building guide was mirrored and did not work. It was missing several jumper wires, had pointless ultrasonic sensors, and overall it just did not work for me. I ended up following separate guides for both the ultrasonic sensor and the H-bridge. The main differences were removing two of the ultrasonic sensors, powering the breadboard (for the ultrasonic sensor) and connecting the H-bridge to ground. The code was another thing that did not work for me; the pins were assigned to the sensors and motors incorrectly, the sleep functions were too short (making the movements very choppy) and a few other functions were formatted incorrectly.
<br>
# Second Milestone: Color Tracking
<iframe width="560" height="315" src="https://www.youtube.com/embed/tGEwsnJFgCQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My second milestone was getting my PiCamera to detect the red ball with OpenCV. For the image analysis, my code takes each frame and masks it so that the PiCamera only detects the red color from the ball. It then detects and dilates the blob that does not get filtered out by the mask. The largest blob is then bound to a blue rectangle in the image analysis window, detecting the center of the rectangle which will be used in my third milestone. 

This code was something I had a very difficult time in as I have very little to no experience in coding. At first, I was just following and correcting any error codes that showed up, however in this process, I accidentally broke other functions in the code, rendering the whole code invalid. I was able to overcome this challenge with the help of the instructors and another student who is doing the same project. I learned a lot of patience through this milestone and that most things will not go right the first or second time. Perseverance and continuing to try different methods to fix problems is very time consuming, yet very rewarding in the end. My next milestone will be to set up the motors so that the robot can follow the ball after it detects the red ball.
<br>
# First Milestone: Robot Assembly
<iframe width="560" height="315" src="https://www.youtube.com/embed/ih8gcHIPG-I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My first milestone was assembling the physical portion of the ball tracking robot. This included the wiring of all of the DC motors, ultrasonic sensors, PiCamera and batteries into the Raspberry Pi, H-Bridge and breadboard. The two motors are connected the two ports on each side of the H-bridge, which is connected to a separate 6V battery pack and wired to the Raspberry Pi. The three ultrasonic sensors have four pins each, two connect to the Raspberry Pi while the other two go to the breadboard. The PiCamera plugs directly onto the camera port on the Raspberry Pi. Finally, all of the components are mounted on a plastic chasis.

The most important part of this process was making sure all of the pins and wires were firmly attached to the different boards. It was important to do this as you do not want the wires disconnecting while the robot is in motion, potentially breaking the connection to important components. It was especially difficulty as the male and female connector cables fit very loose on the Raspberry Pi and breadboard. My next milestone will be to get the motors to function so the robot will be able to follow the ball in the final design.


<!---# Schematics--> 


# Code

from picamera.array import PiRGBArray

from picamera import PiCamera

import RPi.GPIO as GPIO

import time

import cv2

import cv2 as cv

import numpy as np

GPIO.setmode(GPIO.BCM)

TRIG = 23      #Front ultrasonic sensor
ECHO = 22

MOTOR1B = 19  #Left Motor pins 1B=2, 1E=1 on H-bridge
MOTOR1E = 26

MOTOR2B = 13  #Right Motor pins 2B=4, 2E=3
MOTOR2E = 6


GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
#GPIO.setup(LED_PIN,GPIO.OUT)

GPIO.output(TRIG, False)

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

camera = PiCamera()
camera.resolution = (160, 128)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(160, 128))

time.sleep(0.001)
 
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
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
      if(found==0):
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
                  if(distanceC<10):
                        forward()
                        time.sleep(0.00625)
            elif(area>=initial):
                  initial2=6700
                  if(area<initial2):
                        if(distanceC>10):
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
                        time.sleep(0.1)
                        stop()
                        time.sleep(0.1)
      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)
         
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break

GPIO.cleanup()

# Bill of Materials

| **Part** | **Note** | **Price** | **Link** |
|:--:|:--:|:--:|:--:|
| 1 Raspberry Pi 4 | Main hub for mechanical components of the robot | $124.99 | <a href="https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Micro SD Card | Provides internal storage for the Raspberry Pi | $19.99 | <a href="https://www.amazon.com/SanDisk-micro-Memory-Card-Tablets/dp/B013TMNKAW/ref=asc_df_B013TMNKAW/?tag=hyprod 20&linkCode=df0&hvadid=312026001792&hvpos=&hvnetw=g&hvrand=6885881945781783765&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-570982703758&psc=1/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 H-Bridge | Powers the motors on the robot | $6.99 | <a href="https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6/ref=asc_df_B014KMHSW6/?tag=hyprod-20&linkCode=df0&hvadid=167139094796&hvpos=&hvnetw=g&hvrand=9827173619272994604&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032171&hvtargid=pla-306436938191&psc=1/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Breadboard | Builds temporary circuits | $5.99 | <a href="https://www.amazon.com/Qunqi-point-Experiment-Breadboard-5-5×8-2×0-85cm/dp/B0135IQ0ZC/ref=asc_df_B0135IQ0ZC/?tag=hyprod-20&linkCode=df0&hvadid=198091709182&hvpos=&hvnetw=g&hvrand=5812493995046974704&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-407203040794&psc=1/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 2 DC Motors | Helps the robot move | $8.77 | <a href="https://www.amazon.com/ApplianPar-Shaft-Gearbox-Plastic-Arduino/dp/B086D5M65M/ref=asc_df_B086D5M65M/?tag=hyprod-20&linkCode=df0&hvadid=459579282194&hvpos=&hvnetw=g&hvrand=4755515537823895031&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-995092589714&psc=1/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 3 Ultrasonic Sensors | Measures the distance between objects and the robot | $15.75 | <a href="https://www.amazon.com/HC-SR04-Ranging-Detector-Ultrasonic-Distance/dp/B01GNEHJNC/ref=asc_df_B01GNEHJNC/?tag=hyprod-20&linkCode=df0&hvadid=312147770792&hvpos=&hvnetw=g&hvrand=1325046763594526637&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-645671517737&psc=1&tag=&ref=&adgrpid=61924583437&hvpone=&hvptwo=&hvadid=312147770792&hvpos=&hvnetw=g&hvrand=1325046763594526637&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-645671517737/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Pi-Cam | Detects objects and materials in front of it | $35.00 | <a href="https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_6?keywords=pi+cam&qid=1687191814&sr=8-6/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Soldering Iron | Melts solder wire to connect circuits | $23.99 | <a href="https://www.amazon.com/Soldering-Iron-Kit-Temperature-Screwdrivers/dp/B07GJNKQ8W/ref=sr_1_4_sspa?crid=3SWW7HN9U1AF1&keywords=20+dollar+soldering+kit&qid=1656613484&sprefix=20+dollar+soldering+kit%2Caps%2C59&sr=8-4-spons&psc=1&smid=A2CEQAD2VNOS6B&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBSkI4UURNT0tRSlomZW5jcnlwdGVkSWQ9QTAwMzg5ODIzVkk0Nk03V1pSTzFRJmVuY3J5cHRlZEFkSWQ9QTA5Nzk4MTIxTUNMRUUwMlpWMlk1JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==/"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Screw Driver Kit | Tightens/loosens screws on the robot | $6.57 | <a href="https://www.amazon.com/Precision-Screwdriver-Screwdrivers-Watchmaker-Electronic/dp/B0BFQK5FVR/ref=asc_df_B0BFQK5FVR/?tag=hyprod-20&linkCode=df0&hvadid=642117690907&hvpos=&hvnetw=g&hvrand=4331594184654728423&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032183&hvtargid=pla-1932769940359&psc=1&gclid=CjwKCAjw-b-kBhB-EiwA4fvKrE_5pwfP_-3qlOAAvzoQTmotyUPMkTqlHCV0bAWt41AqeLGUcLoBGhoCzP4QAvD_BwE"> Link </a> |
|:--:|:--:|:--:|:--:|
| 1 Jumper Wire Set | Connects circuits andd transfer voltage | $9.99 | <a href="https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/"> Link </a> |
|:--:|:--:|:--:|:--:|

# Starter Project: Simon Says
<iframe width="560" height="315" src="https://www.youtube.com/embed/wQZZTsq8bbo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My starter project is the game Simon. This game flashes LEDs and the player is supposed to memorize and repeat the pattern. With each press on the button pad, the corresponding LED lights up and a buzzing sound is played. In this project, I learned about the function of different components that I had never used before, more specifically, microcontrollers and decoupling capacitors. One thing that I had a difficult time with was desoldering and this helped me realize just how hard it is to take a component out of a PCB once it has been soldered in.

# Links to Guides/Manufacturers
[Ball Tracking Robot](https://www.hackster.io/junejarohan/ball-tracking-robot-7a9865)

[Robot Arm](https://github.com/Cokoino/CKK0006)

[Simon Says](https://www.sparkfun.com/products/10547)

