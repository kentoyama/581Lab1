#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
stop_type = Stop.COAST
right.run_time(613.88, 4400, Stop.BRAKE, False)
left.run_time(613.88, 4400, Stop.BRAKE, True)
right.stop()
left.stop()
wait(1000)
brick.sound.beep()
while not Button.CENTER in brick.buttons():
    wait(10)


ultrasonicSensor = UltrasonicSensor(Port.S1)
stop_type = Stop.COAST

while ultrasonicSensor.distance() > 515 or ultrasonicSensor.distance() < 485: # + distance the sensor is from the front of the robot
    
    if ultrasonicSensor.distance() > 515:
        right.run(200)
        left.run(215)
        wait(100)
        right.stop()
        left.stop()
    if ultrasonicSensor.distance() < 485:
        right.run(-200)
        left.run(-215)
        wait(100)
        right.stop()
        left.stop()
wait(1000)
brick.sound.beep()
while not Button.CENTER in brick.Buttons():
    wait(10)


TouchSensorR = TouchSensor(Port.S2)
TouchSensorL = TouchSensor(Port.S4)
while TouchSensorR.pressed() == False and TouchSensorL.pressed() == False:
    right.run(360)
    left.run(361)

right.stop()
left.stop()

while ultrasonicSensor.distance() > 510 or ultrasonicSensor.distance() < 490:
    if ultrasonicSensor.distance() > 510:
         right.run(200)
         left.run(210)
         wait(100)
         right.stop()
         left.stop()
    if ultrasonicSensor.distance() < 490:
         right.run(-200)
         left.run(-215)
         wait(100)
         right.stop()
         left.stop()
wait(1000)
brick.sound.beep()
