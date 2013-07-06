#! /usr/bin/env python
import pygame, random
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Splash:
	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((400,200), False)
		self.background = pygame.Surface(self.screen.get_size())

		self.running = True
		
		self.background = self.background.convert()
		
		self.splashImage = pygame.image.load("data\\splash.png")
		self.splashImage = self.splashImage.convert()
			
	def main(self):
		while self.running:
			for n in range(255):
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(n)
				self.screen.blit(self.splashImage,(0,0))
				pygame.display.flip()
				pygame.time.delay(15)

			pygame.time.delay(2000)

			self.splashImage = pygame.image.load("data\\splash.png")
			self.splashImage = self.splashImage.convert()
			
		
			for n in range(255):
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(255-n)
				self.screen.blit(self.splashImage,(0,0))
				pygame.display.flip()
				pygame.time.delay(15)
				
			self.running = False
		pygame.quit()


splash = Splash()
splash.init()
splash.main()