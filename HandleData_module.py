#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Program created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
OS: Windows 7
Pythonversion: 2.7.5

This class handles the read and write to file part of my Tetris application.
Obviouslt this can be reused in other programs as all it does is read the files line per line.

"""
import pygame, random, os.path
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class HandleData:
	#Method that reads the option file. This will read the lines and check for the values "False" and "True" and append to the list.
	#The list will be returned for the caller. The check if the data is what expected is left to the caller.
	def readOptions(self):
		options = []
		try:
			the_file = open(os.path.join('data','options.txt'), "r")
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
	#Writes the data to the option file. Will not append to an existing file but overwrite.
	def writeOptions(self, listToPrint):
		try:
			the_file = open(os.path.join('data','options.txt'), "w")
		
		except(IOError), e:
			print "Nu gick något fel!", e
			raw_input("Tryck på valfri tangent för att avsluta.")
			sys.exit()
		
		else:
			for item in listToPrint:
				the_file.write(str(item) + "\n")
			
			the_file.close()
	#Reads the highscore data from the file "highscore.txt". file. Reads this line per line, and assumes that the player have not tinkered with the file.
	#This will first read the name, and remove the \n char. and after that it will read the next line which should hold the score data.
	def readData(self):
		self.highscoreList = []
		self.newPlayer = True
		try:
			the_file = open(os.path.join('data','highscore.txt'), "r")
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
	#Writes the highscoredata, just as the option method this will overwrite any existing file.
	def writeData(self, listToPrint):
		
		try:
			the_file = open(os.path.join('data','highscore.txt'), "w")
		
		except(IOError), e:
			print "Nu gick något fel!", e
			raw_input("Tryck på valfri tangent för att avsluta.")
			sys.exit()
		
		else:
			for item in listToPrint:
				the_file.write(item[0] + "\n")
				the_file.write(str(item[1]) + "\n")				
			
			the_file.close()
	#Reads the help file. As there is no reason to write to this file no such method exists.
	def readAbout(self):
		options = []
		try:
			the_file = open(os.path.join('data','about.txt'), "r")
		except(IOError), e:
			print "Something went wrong! Data file not found.", e

		else:
			for line in the_file:
				line = line.replace("\n", "")
				options.append(line)
			return options
			