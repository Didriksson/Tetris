#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
This class will display a sort of Intro or a splash image if you like. It will fade the image in, as well as fade it out.
OS: Windows 7
Pythonversion: 2.7.5
"""
import pygame, random, os.path, Menu_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Splash():

	#Entry point for the splash class.
	def start(self):
		self.init()
		self.main()

	#Initializes the attributes of the class.
	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((500,600), False)
		self.background = pygame.Surface(self.screen.get_size())

		self.finnished = False
		self.count = 0
		self.fadeIn = True
		self.running = True
		self.clock = pygame.time.Clock()
		self.background = self.background.convert()
		
		self.splashImage = pygame.image.load(os.path.join('data\Graphics','splash.png'))
		self.splashImage = self.splashImage.convert()
			
	#Handles the fade in effect as well as the fade out.
	def fade(self):
			if not self.fadeIn:
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(self.count)
				self.screen.blit(self.splashImage,(50,150))
				pygame.display.flip()
				self.count = self.count - 4
				if self.count <0:
					self.fadeIn = False
					self.running = False

					
			if self.fadeIn:
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(self.count)
				self.screen.blit(self.splashImage,(50,150))
				pygame.display.flip()
				self.count = self.count + 4
				if self.count > 254:
					self.fadeIn = False
					pygame.time.delay(500)
				
	#This is the loop that runs in order to check for key events. This is made so that the player can skip the intro if he wants.
	#Will also handle the call for the fade method.
	def main(self):
		while self.running:
			self.fade()
			self.clock.tick(20)
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
			
				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						self.running = False
					if e.key == K_RETURN:
						self.running = False
					
					
		menu = Menu_module.Menu()
		menu.start(self.screen)
