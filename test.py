#Required Imports
from pymycobot.mypalletizer import MyPalletizer
from pymycobot.genre import Coord
import time
import RPi.GPIO as GPIO

#Speed for thge robot
mySpeed = 20

#Robot Initilization 
mc = MyPalletizer('/dev/ttyAMA0',1000000)
mc.power_on

#Initilization for the phneoumatic system of the robot
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)

#Moves robbot to an initilization angle
initilization_angle = [0, 0, 0, 0]
mc.send_angles(initilization_angle, mySpeed)

#The for loop which range is determined by the number of blochs
for i in range(2):

    while 1:
            if mc.is_moving() == 0:
                break

    mc.send_angles(pickup_angle, mySpeed)
    pickUpPos = mc.get_coords()
    time.sleep(2)     
    GPIO.output(20,GPIO.LOW)
    time.sleep(1)
    while 1:
            if mc.is_moving() == 0:
                break
  
    print(pickUpPos)
    
    mc.send_angles(initilization_angle, mySpeed) 
    
    while 1:
            if mc.is_moving() == 0:
                break
                            
    mc.send_coord(Coord.Y.value, pickUpPos[1] * -1 ,20)
    time.sleep(1)
    GPIO.output(20,GPIO.HIGH)
    time.sleep(1)
print("bum")

