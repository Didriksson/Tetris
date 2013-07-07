#! /usr/bin/env python
import pygame, random, os.path
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Splash:
	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((400,200), False)
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
				self.screen.blit(self.splashImage,(0,0))
				pygame.display.flip()
				print self.count
				if self.count <0:
					self.fadeIn = False
					self.running = False

					
			if self.fadeIn:
				self.background.fill((0,0,0))
				self.screen.fill((0,0,0))
				self.splashImage.set_alpha(self.count)
				self.screen.blit(self.splashImage,(0,0))
				pygame.display.flip()
				self.count = self.count + 1
				if self.count > 254:
					self.fadeIn = False
					pygame.time.delay(1000)
				
		
	def main(self):
		while self.running:
			self.fade()
			self.clock.tick(40)
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
			
				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						self.running = False
					
		menu = Menu()
		menu.start()
		
		

		
class Menu:
	
	def start(self):
		self.init()
		self.main()

	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((400, 600), False)

		self.button = pygame.image.load(os.path.join('data','button.png'))
		self.markedButton = pygame.image.load(os.path.join('data','markedButton.png'))
		
		self.choice = 0
		
		self.background = pygame.image.load(os.path.join('data','menu.png'))
		pygame.display.flip()
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.font = pygame.font.SysFont("SKETCHFLOW PRINT", 30)
		self.start = self.font.render("START", True, (0, 0, 0))
		self.highscore = self.font.render("HIGHSORE", True, (0, 0, 0))
		self.options = self.font.render("OPTIONS", True, (0, 0, 0))
		self.quit = self.font.render("QUIT", True, (0, 0, 0))
		
	def main(self):
		while self.running:
			self.screen.blit(self.background,(0,0))
			for n in range(4):
				if self.choice == n:
					self.screen.blit(self.markedButton, (40,n * 110 + 140))
				else:
					self.screen.blit(self.button, (40,n * 110 + 140))
			
			self.screen.blit(self.start, (155, 152))
			self.screen.blit(self.options, (140, 262))
			self.screen.blit(self.highscore, (135, 372))
			self.screen.blit(self.quit, (165, 482))
			pygame.display.flip()
			self.clock.tick(20)
			
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
				if e.type == KEYDOWN:
					if e.key == K_DOWN:
						if (self.choice < 3):
							self.choice += 1
					if e.key == K_UP:
						if (self.choice > 0):
							self.choice -= 1
			
		pygame.quit()
			
splash = Splash()
splash.init()
splash.main()