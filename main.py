#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
motor_right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robot = DriveBase(motor_left, motor_right, 56, 130)
robot.drive_time(300, 0, 4000)
brick.sound.beep()

ultrasonicSensor = UltrasonicSensor(port)
while ultrasonicSensor.distance() > 500: # + distance the sensor is from the front of the robot
    robot.drive(300, 0)
    wait(5)
brick.sound.beep()
while not button.CENTER in brick.buttons():
    wait(10)
