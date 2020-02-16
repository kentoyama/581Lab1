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
robot.drive_time(300, 0, 3900)
wait(1000)
brick.sound.beep()
while not Button.CENTER in brick.buttons():
    wait(10)


ultrasonicSensor = UltrasonicSensor(Port.S1)

while ultrasonicSensor.distance() > 530 or ultrasonicSensor.distance() < 470: # + distance the sensor is from the front of the robot
    if ultrasonicSensor.distance() > 530:
        robot.drive(150,0)
    if ultrasonicSensor.distance() < 470:
        robot.drive(-150, 0)
wait(1500)
while ultrasonicSensor.distance() > 505 or ultrasonicSensor.distance() < 495: # + distance the sensor is from the front of the robot
    if ultrasonicSensor.distance() > 505:
        robot.drive(50,0)
    if ultrasonicSensor.distance() < 495:
        robot.drive(-50, 0)
wait(500)
brick.sound.beep()
while not button.CENTER in brick.Buttons():
    wait(10)

