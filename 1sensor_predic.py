#!/usr/bin/env python3
import numpy as np
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
import time


"""load up peripherals. sensors motors buttons etc"""
button = Button()
l_sensor3 = ColorSensor(INPUT_3)
l_sensor1 = ColorSensor(INPUT_1)
u_sensor = UltrasonicSensor()
sound = Sound()

def return_pressed_button(button):
    """waits for center button to be pressed and then returns the button object"""
    
    pressed_button = None
    while True:
        sound.play_tone(400, 0.5)
        #print(button.buttons_pressed)
        print("press button:")
        if button.enter:
            print(button.enter)
            sound.play_tone(300, 0.5)
            pressed_button = button
            break
    return True, pressed_button
        

def record_light(duration=3, N=100):
    """records light levels for given number of secs seconds and calculates average"""
    start_time = time.time()
    t_elapsed = time.time() - start_time
    #l_sensor = ColorSensor(INPUT_1)
    l_arr = []
    for i in range(0, N):
    #while t_elapsed < duration:
        l_arr.append(l_sensor1.ambient_light_intensity)
        t_elapsed = time.time() - start_time
    print(N, "recordings done in ", t_elapsed)
    return l_arr


def ave_l_levels(button):
    """gets the mean light reading. ideally robot will be stationary so it is just for that distance"""
    #start program
    pressed, button = return_pressed_button(button)
    mean = 0
    if pressed:
        l_levels = record_light()
        mean = sum(l_levels)/len(l_levels)
    return mean

""""
while True:
    print("light intensity at start", l_sensor.ambient_light_intensity)
"""
#mean = ave_l_levels(button)
#record 3 different levels
means = []
for i in range(0,15):
    means.append(ave_l_levels(button))

print("results", means)



"""
In this example we infer one hidden state distance X
Robot is to remain static in one location
We assume the generative model has already been learned (ie how light reading is related to distance)
"""