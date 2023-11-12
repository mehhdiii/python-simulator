from __future__ import print_function

import time
import pprint
from sr.robot import *

def moveStraight(R, t):
    '''Moves the robot in a straight line for t seconds in forward direction'''
    R.motors[0].m0.power = 50
    R.motors[0].m1.power = 50
    time.sleep(t)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def moveBack(R, t):
    '''Moves the robot in a straight line for t seconds in backwards direction'''
    R.motors[0].m0.power = -50
    R.motors[0].m1.power = -50
    time.sleep(t)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0 

def spinRight(R, t):
    '''Spins the robot for t seconds in clockwise direction'''
    R.motors[0].m0.power = 50
    R.motors[0].m1.power = -50
    time.sleep(t)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def spinLeft(R, t):
    '''Spins the robot for t seconds in anti-clockwise direction'''
    R.motors[0].m0.power = -50
    R.motors[0].m1.power = 50
    time.sleep(t)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


def MoveTowardsObject(R):
    '''Moves the robot towards the object by self-adjusting pose to grab it'''
    while True:
        print(R.see()[0].dist, R.see()[0].rot_y)
        if R.see()[0].dist < 0.4:
            R.grab()
            break
        elif R.see()[0].rot_y > 5:
            spinRight(R, 0.01)
            moveStraight(R, 0.1)
        elif R.see()[0].rot_y < -5:
            spinLeft(R, 0.01)
            moveStraight(R, 0.1)  
        else:
            moveStraight(R, 0.01)  
R = Robot()

#STEPS: 
#1. initially align the robot towards the object.
#2. move the robot towards the object while self adjusting its pose. Grab the object when it is close enough.
#3. move the robot back to the center and release the object.

#NOTES: 
#1. We hard code picking up the first object
#2. All other objects are picked up by moving the robot towards the object and self adjusting its pose.

#pick and drop first object to the center
moveStraight(R, 1.25)
spinRight(R, 0.3)
moveStraight(R, 1.5)
print(R.see())
R.grab()
moveStraight(R, 1.3)
spinLeft(R, 0.6)
moveStraight(R, 2.2)
print(R.release())
moveBack(R, 2.3)

# #pick and drop second object to the center
spinRight(R, 0.7)
MoveTowardsObject(R)
moveBack(R, 1.2)
spinLeft(R, 0.58)
moveStraight(R, 2.8)
R.release()
moveBack(R, 2.3)

# pick and drop third object to the center
spinRight(R, 0.4)
MoveTowardsObject(R)
spinLeft(R, 0.8)
moveStraight(R, 3)
R.release()
moveBack(R, 1)

# pick and drop fourth object to the center
spinRight(R, 0.6)
MoveTowardsObject(R)
spinLeft(R, 1)
moveStraight(R, 3)
R.release()
moveBack(R, 1)

# pick and drop fifth object to the center
spinRight(R, 0.7)
MoveTowardsObject(R)
spinLeft(R, 1)
moveStraight(R, 3)
R.release()
moveBack(R, 1)

# pick and drop sixth object to the center
spinRight(R, 0.6)
MoveTowardsObject(R)
spinLeft(R, 1)
moveStraight(R, 3)
R.release()
moveBack(R, 1)
