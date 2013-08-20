#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
This class takes care of handling the menu from which the player can select what action to take.
OS: Windows 7
Pythonversion: 2.7.5
"""

import pygame, random, os.path, Tetris, HandleData_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class Menu():
	
	#A method created as an entry to the class. This will make sure that the screen is passed on and contact the current methods in sequence.
	def start(self, screen):
		self.init(screen)
		self.main()
	#Initiates most of the resources that the menu class utilizes.
	def init(self, sentScreen):
		
		self.screen = sentScreen

		#Loads the resources.
		self.button = pygame.image.load(os.path.join('data\Graphics','button.png'))
		self.markedButton = pygame.image.load(os.path.join('data\Graphics','markedButton.png'))
		self.background = pygame.image.load(os.path.join('data\Graphics','menu.png'))
		
		self.choice = 0
		
		pygame.display.flip()
		self.running = True
		self.clock = pygame.time.Clock()
		
		#Initializes the fonts.
		self.highscoreFont = pygame.font.SysFont("Arial Black", 20)
		self.font = pygame.font.SysFont("SKETCHFLOW PRINT", 30)
		self.headerFont = pygame.font.SysFont("SKETCHFLOW PRINT", 40)
		self.helpFont = pygame.font.SysFont("Arial Black", 12)

		
		#Render the texts.
		self.highscoreHeaderText = self.headerFont.render("Highscore", True, (171,4,4))
		self.optionsHeaderText = self.headerFont.render("Options", True, (171,4,4))
		self.helpHeaderText = self.headerFont.render("Help", True, (171,4,4))
		self.mainHeaderText = self.headerFont.render("pyTetris", True, (171,4,4))
		self.start = self.font.render("START", True, (0, 0, 0))
		self.highscore = self.font.render("HIGHSORE", True, (0, 0, 0))
		self.help = self.font.render("HELP", True, (0,0,0))
		self.optionsText = self.font.render("OPTIONS", True, (0, 0, 0))
		self.quit = self.font.render("QUIT", True, (0, 0, 0))
		
	#Main loop of this class. Takes care of displaying the main menu as well as handling key events.	
	def main(self):
		#As this loop will be the first(except for splash) and last the player sees if existing correctly, this loop will run until player either presses the X in the corner or
		#chooses the quit option within the menu.
		while self.running:
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.mainHeaderText,(165,20))
			#Keeps track of the marked button in the menu and will print out the correct button accordingly.
			for n in range(5):
				if self.choice == n:
					self.screen.blit(self.markedButton, (90,n * 80 + 130))
				else:
					self.screen.blit(self.button, (90,n * 80 + 130))
			#Prints the texts on the buttons.
			self.screen.blit(self.start, (205, 145))
			self.screen.blit(self.optionsText, (190, 225))
			self.screen.blit(self.highscore, (185, 305))
			self.screen.blit(self.help, (215, 385))
			self.screen.blit(self.quit, (215, 465))
			pygame.display.flip()
			self.clock.tick(20)
			
			#Event handler that will listen for key events and handle them accordingly.
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
				if e.type == KEYDOWN:
					if e.key == K_DOWN:
						if (self.choice < 4):
							self.choice += 1
					if e.key == K_UP:
						if self.choice > 0:
							self.choice -= 1

					#This listens for the return key, and will do the action that the user have picked.
					#Most notably is the "START" option that need to keep track of a lot of parameters. It will check
					#for the action returned from the game as well as check the settings before starting.
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
								nextAction = Tetris.start(self.screen, grid, sound)
							if nextAction == "MENU":
								pass
						elif self.choice == 1:
							self.running = self.displayOptions()
						elif self.choice == 2:
							self.running = self.displayHighscore()
						elif self.choice == 3:
							self.running = self.displayHelp()
						elif self.choice == 4:
							self.running = False
		
		pygame.quit()
	#Method that will display the help page.
	def displayHelp(self):
		data = HandleData_module.HandleData()
				
		pressedKey = False
		self.pressAnyKeyFont = pygame.font.SysFont("SKETCHFLOW PRINT", 30)
		self.pressAnyKeyText = self.pressAnyKeyFont.render("Press any key to return.", True, (0,0,0))
		self.listOfHelpText = data.readAbout()
		while not pressedKey:

			self.screen.fill((0,0,0))
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.helpHeaderText,(220,20))
			self.screen.blit(self.pressAnyKeyText,(50,550))
			for index, line in enumerate(self.listOfHelpText):
				self.aboutText = self.helpFont.render(line, True, (0,0,0))
				self.screen.blit(self.aboutText, (100, index * 15 + 100))
				
			
			pygame.display.flip()
			self.clock.tick(20)
			
			for e in pygame.event.get():
				if e.type == KEYDOWN:
					pressedKey = True
				if e.type == QUIT:
					return False
					
		return True	
	#Method that displays the option page. Currently there is only the option to turn off sound and the grid layout.
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
	#Displays the highscore.	
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