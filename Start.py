#! /usr/bin/env python
import pygame, random, os.path, Tetris
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Splash:
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
					
		menu = Menu()
		menu.start(self.screen)
		
		

		
class Menu():
	
	def start(self, screen):
		self.init(screen)
		self.main()

	def init(self, sentScreen):
		
		self.screen = sentScreen

		self.button = pygame.image.load(os.path.join('data','button.png'))
		self.markedButton = pygame.image.load(os.path.join('data','markedButton.png'))
		
		self.choice = 0
		
		self.background = pygame.image.load(os.path.join('data','menu.png'))
		pygame.display.flip()
		self.running = True
		self.clock = pygame.time.Clock()
		
		self.highscoreFont = pygame.font.SysFont("Arial Black", 20)
		self.font = pygame.font.SysFont("SKETCHFLOW PRINT", 30)
		self.headerFont = pygame.font.SysFont("SKETCHFLOW PRINT", 40)
		

		self.highscoreHeaderText = self.headerFont.render("Highscore", True, (171,4,4))
		self.mainHeaderText = self.headerFont.render("pyTetris", True, (171,4,4))
		self.start = self.font.render("START", True, (0, 0, 0))
		self.highscore = self.font.render("HIGHSORE", True, (0, 0, 0))
		self.options = self.font.render("OPTIONS", True, (0, 0, 0))
		self.quit = self.font.render("QUIT", True, (0, 0, 0))
		
	def main(self):
		while self.running:
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.mainHeaderText,(165,20))
			for n in range(4):
				if self.choice == n:
					self.screen.blit(self.markedButton, (90,n * 110 + 140))
				else:
					self.screen.blit(self.button, (90,n * 110 + 140))
			
			self.screen.blit(self.start, (205, 152))
			self.screen.blit(self.options, (190, 262))
			self.screen.blit(self.highscore, (185, 372))
			self.screen.blit(self.quit, (215, 482))
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
						if self.choice > 0:
							self.choice -= 1

							
					if e.key == K_RETURN:
						if self.choice == 0:
							nextAction = Tetris.start(self.screen)
							if nextAction == "QUIT":
								self.running = False
							if nextAction == "AGAIN":
								nextAction = Tetris.start(self.screen)
							if nextAction == "MENU":
								pass
						if self.choice == 1:
							pass
						if self.choice == 2:
							self.displayHighscore()
							
						if self.choice == 3:
							self.running = False
		
		pygame.quit()
	
	def displayHighscore(self):
		name = ""
		score = ""
		data = Tetris.HandleData()
		currentHighscoreList = data.readData()
		pressedKey = False
		print currentHighscoreList
		while not pressedKey:
			self.screen.fill((0,0,0))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.highscoreHeaderText,(165,20))
			
			for i in range(20):
				position = self.highscoreFont.render(str(i + 1).zfill(2) + ".", True,(0,0,0))
				self.screen.blit(position, (120, ( 21 * i) + 110))

			
			for index, item in enumerate(currentHighscoreList):
				name  = self.highscoreFont.render(item[0], True,(0,0,0))
				score = self.highscoreFont.render(str(item[1]).zfill(6), True,(0,0,0))
				self.screen.blit(name, (195,(21 * index) + 110))
				self.screen.blit(score, (300,(21 * index) + 110))				
			
			pygame.display.flip()
			self.clock.tick(20)
			
			for e in pygame.event.get():
				if e.type == KEYDOWN:
					pressedKey = True

menu = Menu()					
splash = Splash()
splash.init()
splash.main()