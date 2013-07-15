#!/usr/bin/env python
# -*- coding: cp1252 -*-

import pygame, random, os.path, Menu_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Splash():

	
	def start(self):
		self.init()
		self.main()


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
		
		self.splashImage = pygame.image.load("data\\splash.png")
		self.splashImage = self.splashImage.convert()
			

	def fade(self):
			if not self.fadeIn:
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(self.count)
				self.screen.blit(self.splashImage,(50,150))
				pygame.display.flip()
				self.count = self.count - 1
				if self.count <0:
					self.fadeIn = False
					self.running = False

					
			if self.fadeIn:
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(self.count)
				self.screen.blit(self.splashImage,(50,150))
				pygame.display.flip()
				self.count = self.count + 1
				if self.count > 254:
					self.fadeIn = False
					pygame.time.delay(1000)
				
		
	def main(self):
		while self.running:
			self.fade()
			self.clock.tick(30)
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
