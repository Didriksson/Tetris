#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Program created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
OS: Windows 7
Pythonversion: 2.7.5

This is a simple Tetris clone, made from scratch by me. 

"""

import pygame, random, os.path, Splash_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

splash = Splash_module.Splash()
splash.start()