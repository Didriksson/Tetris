#!/usr/bin/env python
# -*- coding: cp1252 -*-

import pygame, random, os.path
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class HandleData:

	def readOptions(self):
		options = []
		try:
			the_file = open("options.txt", "r")
		except(IOError), e:
			print "Something went wrong! Data file not found.", e

		else:
			for line in the_file:
				line = line.replace("\n", "")
				if line == "True":
					options.append(True)
				elif line == "False":
					options.append(False)
			return options

	def writeOptions(self, listToPrint):
		try:
			the_file = open("options.txt", "w")
		
		except(IOError), e:
			print "Nu gick något fel!", e
			raw_input("Tryck på valfri tangent för att avsluta.")
			sys.exit()
		
		else:
			for item in listToPrint:
				the_file.write(str(item) + "\n")
			
			the_file.close()
			
	def readData(self):
		self.highscoreList = []
		self.newPlayer = True
		try:
			the_file = open("data.txt", "r")
		except(IOError), e:
			print "Something went wrong! Data file not found.", e

		else:

			for line in the_file:
				if self.newPlayer:
					self.player = line
					self.player = self.player.replace("\n", "")
					self.newPlayer = False
				elif not self.newPlayer:
					self.score = line
					self.score = self.score.replace("\n", "")
					self.newPlayer = True
					self.highscoreList.append((self.player, int(self.score)))

			the_file.close()
		return self.highscoreList

	def writeData(self, listToPrint):
		
		try:
			the_file = open("data.txt", "w")
		
		except(IOError), e:
			print "Nu gick något fel!", e
			raw_input("Tryck på valfri tangent för att avsluta.")
			sys.exit()
		
		else:
			for item in listToPrint:
				the_file.write(item[0] + "\n")
				the_file.write(str(item[1]) + "\n")				
			
			the_file.close()
