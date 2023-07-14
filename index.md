# Ball Tracking Robot
My project is a ball tracking robot, which as indicated by the name, tracks and follows a red ball. This robot utilizes computer vision in order to find and track an object with a fixed color.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Alex L. | Sequoia High School | Mechanical Engineering | Incoming Sophomore
<br>

# Modification: Robot Arm
My modification to my ball tracking robot is a robot arm. This kit by Cokoino is a a 4-axis robotic arm, powered by an Arduino nano, moves using servo motors and controlled using a joystick controller. This was one of the easiest milestones/parts of this project because pretty much the entire kit worked when first assembled; it required significantly less troubleshooting compared to the other three milestones. One thing I needed to change from the original kit was the battery pack. This was because we did not have the two 18650 batteries that would fit into the original battery pack. I replaced it with a AA pack with 5 slots because the AA batteries supply much less voltage than the 18650s. 

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

My second milestone was getting my PiCamera to detect the red ball with OpenCV. For the image analysis, my code takes each frame and masks it so that the PiCamera only detects the red color from the ball. It then detects and dilates the blob that does not get filtered out by the mask. The largest blob is then bound to a blue rectangle in the image analysis window, detecting the center of the rectangle which will be used in my third milestone. This code was something I had a very difficult time in as I have very little to no experience in coding. At first, I was just following and correcting any error codes that showed up, however in this process, I accidentally broke other functions in the code, rendering the whole code invalid. I was able to overcome this challenge with the help of the instructors and another student who is doing the same project. I learned a lot of patience through this milestone and that most things will not go right the first or second time. Perseverance and continuing to try different methods to fix problems is very time consuming, yet very rewarding in the end. My next milestone will be to set up the motors so that the robot can follow the ball after it detects the red ball.
<br>
# First Milestone: Robot Assembly
<iframe width="560" height="315" src="https://www.youtube.com/embed/ih8gcHIPG-I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My first milestone was assembling the physical portion of the ball tracking robot. This included the wiring of all of the motors, sensors and batteries into the Raspberry Pi, H-Bridge and breadboard. The most important part of this process was making sure all of the pins and wires were firmly attached to the different boards. It was important to do this as you do not want the wires disconnecting while the robot is in motion, potentially breaking the connection to important components. It was especially difficulty as the male and female connector cables fit very loose on the Raspberry Pi and breadboard. My next milestone will be to get the motors to function so the robot will be able to follow the ball in the final design.


<!---# Schematics--> 


<!---# Code-->


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

# Starter Project
<iframe width="560" height="315" src="https://www.youtube.com/embed/wQZZTsq8bbo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

My starter project is the game Simon. This game flashes LEDs and the player is supposed to memorize and repeat the pattern. With each press on the button pad, the corresponding LED lights up and a buzzing sound is played. In this project, I learned about the function of different components that I had never used before, more specifically, microcontrollers and decoupling capacitors. One thing that I had a difficult time with was desoldering and this helped me realize just how hard it is to take a component out of a PCB once it has been soldered in.
