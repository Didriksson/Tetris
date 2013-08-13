#!/usr/bin/env python
# -*- coding: cp1252 -*-

import pygame, random, os.path, Tetris, HandleData_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

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
		self.optionsHeaderText = self.headerFont.render("Options", True, (171,4,4))
		self.mainHeaderText = self.headerFont.render("pyTetris", True, (171,4,4))
		self.start = self.font.render("START", True, (0, 0, 0))
		self.highscore = self.font.render("HIGHSORE", True, (0, 0, 0))
		self.optionsText = self.font.render("OPTIONS", True, (0, 0, 0))
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
			self.screen.blit(self.optionsText, (190, 262))
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
							grid = ""
							sound = ""
							data = HandleData_module.HandleData()
							options = data.readOptions()
							if len(options) > 0:
								grid = options[0]
								sound = options[1]

							if (grid == True or grid == False ) and (sound == True or sound == False):
								nextAction = Tetris.start(self.screen, grid, sound)
							else:
								nextAction = Tetris.start(self.screen, True, False)

							if nextAction == "QUIT":
								self.running = False
							if nextAction == "AGAIN":
								nextAction = Tetris.start(self.screen)
							if nextAction == "MENU":
								pass
						elif self.choice == 1:
							self.running = self.displayOptions()
						elif self.choice == 2:
							self.running = self.displayHighscore()
							
						elif self.choice == 3:
							self.running = False
		
		pygame.quit()
	
	
	def displayOptions(self):
		
		self.markedItem = 0
		self.data = HandleData_module.HandleData()
		self.options = self.data.readOptions()
		self.gridOption = True
		self.soundOption = True
		
		if len(self.options):
			if self.options[0] == True or self.options[0] == False:
				self.gridOption = self.options[0]
				
			if self.options[1] == True or self.options[1] == False:
				self.soundOption = self.options[1]
				
		self.quitPressed = False
		
		
		self.soundEnable = self.font.render("ENABLE SOUND", True, (0, 0, 0))
		self.soundDisable = self.font.render("DISABLE SOUND", True, (0, 0, 0))
		self.gridEnable = self.font.render("ENABLE GRID", True, (0, 0, 0))
		self.gridDisable = self.font.render("DISABLE GRID", True, (0, 0, 0))

		
		
		while not self.quitPressed:
			self.screen.fill((0,0,0))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.optionsHeaderText,(165,20))
			
			
				
			for n in range(3):
				if self.markedItem == n:
					self.screen.blit(self.markedButton, (90,n * 110 + 140))
				else:
					self.screen.blit(self.button, (90,n * 110 + 140))
	
			if self.gridOption:
				self.screen.blit(self.gridDisable, (130, 262))
			else:
				self.screen.blit(self.gridEnable, (130, 262))
			
			if self.soundOption:
				self.screen.blit(self.soundDisable, (120, 152))
			else:
				self.screen.blit(self.soundEnable,(120,152))
			self.screen.blit(self.quit, (215, 372))
			
			pygame.display.flip()
						
			for e in pygame.event.get():
				if e.type == KEYDOWN:
					if e.key == K_DOWN:
						if (self.markedItem < 2):
							self.markedItem += 1
					if e.key == K_UP:
						if self.markedItem > 0:
							self.markedItem -= 1
					if e.key == K_RETURN:
						if self.markedItem == 0:
							self.soundOption = not self.soundOption
						elif self.markedItem == 1:
							self.gridOption = not self.gridOption
						elif self.markedItem == 2:
							optionsSaveList = []
							optionsSaveList.append(self.gridOption)
							optionsSaveList.append(self.soundOption)
							self.data.writeOptions(optionsSaveList)
							self.quitPressed = True
				
				if e.type == QUIT:
					return False
			
			self.clock.tick(20)
	
					
		return True
		
		
	def displayHighscore(self):
		name = ""
		score = ""
		data = HandleData_module.HandleData()
		currentHighscoreList = data.readData()
		currentHighscoreList.sort(key = itemgetter(1))
		currentHighscoreList.reverse()
		
		pressedKey = False
		self.pressAnyKeyFont = pygame.font.SysFont("SKETCHFLOW PRINT", 30)
		self.pressAnyKeyText = self.pressAnyKeyFont.render("Press any key to return.", True, (0,0,0))
		while not pressedKey:
			self.screen.fill((0,0,0))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.highscoreHeaderText,(165,20))
			self.screen.blit(self.pressAnyKeyText,(50,550))
			
			for i in range(20):
				position = self.highscoreFont.render(str(i + 1).zfill(2) + ".", True,(0,0,0))
				self.screen.blit(position, (55, ( 21 * i) + 110))

			
			for index, item in enumerate(currentHighscoreList):
				name  = self.highscoreFont.render(item[0], True,(0,0,0))
				score = self.highscoreFont.render(str(item[1]).zfill(6), True,(0,0,0))
				self.screen.blit(name, (90,(21 * index) + 110))
				self.screen.blit(score, (375,(21 * index) + 110))				
			
			pygame.display.flip()
			self.clock.tick(20)
			
			for e in pygame.event.get():
				if e.type == KEYDOWN:
					pressedKey = True
				if e.type == QUIT:
					return False
					
		return True