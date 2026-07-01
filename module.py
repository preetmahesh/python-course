# flask for web apps(a module helpful)
# pip to install a module (its package manager for python)

# math module -- to effectively implement calculations demanding the use of mathematical functions, like sin() or log().

"""
TWO types of modules
1- built in modules (preinstalled in python)
2- external modules (need to install using pip)

"""
# pyttsx3 external module for text to speech

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Preet is trying to learn istg")
# engine.runAndWait


## alt + tap on places to add text at once in all lines
## alt + shift to copy that line and paste down

import math
print(math.sin(math.pi/2))  #sin(1/2 pi)

from math import pi # the listed entities (and only those ones) are imported from the indicated module
# name cnflicts if from module import *

import math as m
# this is aliasing, we use m now for math's name module
# m.sin or m.pi