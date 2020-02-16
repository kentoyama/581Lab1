#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
motor_right = Motor(Port.B, Direction.COUNTERCLOCKWISE) #initialize right motor
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE) #initialize left motor
robot = DriveBase(motor_left, motor_right, 56, 130) #connects both motors to singular robot
robot.drive_time(300, 0, 4000) #300 mm/s for 4000 ms  = 1200 mm travelled
brick.sound.beep()

while not Button.CENTER in brick.buttons():
    wait(10)

ultrasonicSensor = UltrasonicSensor(port)
while ultrasonicSensor.distance() > 500: # + distance the sensor is from the front of the robot
    robot.drive_time(300, 0, 2)
brick.sound.beep()
while not button.CENTER in brick.buttons():
    wait(10)
