Python Robotics Simulator
================================

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Installing and running
----------------------

For Installation steps and API, see [this repository](https://github.com/CarmineD8/python_simulator)

Flow chart
----------------------
This simulation was designed to nagivate using the following philosophy. For each Object i in object_list: 

  1. Partially align the robot towards the object i.
  
  2. Until the object is reached, move the robot in a straight line towards object i while perfoming course correction. We can perform course correction by use of (y-angle-from-object) available to us from the onboard radar sensor:
  - If y-angle-from-object is positive, we rotate the robot slightly towards right.
  - If y-angle-from-ojbect is negative, we rotate the robot slightly towards left.
  - If the object is close enough (distance-from-object < threshold-distance), then pick up the object and Goto step 3.
  - Goto step 2
  
  3. move the robot towards the center and drop the object i there.
