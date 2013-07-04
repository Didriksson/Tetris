"""
Program created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
OS: Windows 7
Pythonversion: 2.7.5

This is a simple Tetris clone, made from scratch by me. 

"""

#! /usr/bin/env python
import pygame, random
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

#The GUI class responsible for most of the program. Reason for that is because the GUI is such a central part of a program like Tetris.
class GUI:
	#A function which will initiate the class. I.e. set up windows, initiate attributes etc.
	def init(self):
		pygame.init()
		
		
		self.blockEmpty = True
		
		self.EMPTY = "EMPTY"
		self.REVERSEL = pygame.image.load("data\\reverseL24.png")
		self.LPIECE = pygame.image.load("data\\Lblock24.png")
		self.LINEPIECE = pygame.image.load("data\\lineBlock24.png")
		self.ZPIECE = pygame.image.load("data\\zBlock24.png")
		self.REVERSEZ = pygame.image.load("data\\reverseZ24.png")
		self.SQUARE = pygame.image.load("data\\square24.png")
		self.TPIECE = pygame.image.load("data\\tSquare24.png")
		
		
		

		font = pygame.font.SysFont("Arial Black", 90)
		self.gameOverImage = font.render("GAME OVER", True, (255, 0, 0))

		self.background = pygame.image.load("data\\background24.png")
		self.topCover = pygame.image.load("data\\topCover24.png")
		
		self.currentPosition = ""
		self.activePiece = []
		self.playArea = []
		self.lines = 22
		self.cols = 10
		
		for line in range(0,self.lines):
			temp = []
			for col in range(0,self.cols):
				temp.append(self.EMPTY)
			self.playArea.append(temp)	

		
		
		self.screen = pygame.display.set_mode((240,528), False)
		
		self.screen.blit(self.background, (0,0))
		
		self.newPiece()
			
		self.reDraw()
		
	#Just as the name states this will take of redrawing the board.	
	def reDraw(self):
		self.screen.blit(self.background,(0,0))
		for indexLine, line in enumerate(self.playArea):
			y = indexLine * 24
			for indexCol, item in enumerate(line):
				x = indexCol * 24
				if(item != "EMPTY"):
					self.screen.blit(item, (x,y))
					self.screen.blit(gui.topCover,(0,0))
					
			
		pygame.display.flip()


	#Adds a piece to the board. Will receive a call from the "new piece" function in order to know which piece to add.	
	def addPiece(self, piece):
	
		if piece == "reverseL":
			self.activePiece = []
			self.playArea[0][4] = self.REVERSEL
			self.playArea[1][4] = self.REVERSEL
			self.playArea[1][5] = self.REVERSEL
			self.playArea[1][6] = self.REVERSEL
			
			self.activePiece = [[0,4], [1,4], [1,5], [1,6]]
			
		if piece == "L":			
			self.playArea[1][4] = self.LPIECE
			self.playArea[1][5] = self.LPIECE
			self.playArea[1][6] = self.LPIECE
			self.playArea[0][6] = self.LPIECE
			self.activePiece = [[1,4], [1,5], [1,6], [0,6]]
			
		if piece == "linePiece":
			self.playArea[0][3] = self.LINEPIECE
			self.playArea[0][4] = self.LINEPIECE
			self.playArea[0][5] = self.LINEPIECE
			self.playArea[0][6] = self.LINEPIECE
			self.activePiece = [[0,3], [0,4], [0,5], [0,6]]
			self.currentPosition = "flat"
			
		if piece == "zPiece":
			self.playArea[0][3] = self.ZPIECE
			self.playArea[0][4] = self.ZPIECE
			self.playArea[1][4] = self.ZPIECE
			self.playArea[1][5] = self.ZPIECE
			self.activePiece = [[0,3], [0,4], [1,4], [1,5]]
			self.currentPosition = "flat"

			
		if piece == "reverseZ":
			self.playArea[1][3] = self.REVERSEZ
			self.playArea[1][4] = self.REVERSEZ
			self.playArea[0][4] = self.REVERSEZ
			self.playArea[0][5] = self.REVERSEZ
			self.activePiece = [[1,3], [1,4], [0,4], [0,5]]
			self.currentPosition = "flat"
			
		if piece == "square":
			self.playArea[0][3] = self.SQUARE
			self.playArea[0][4] = self.SQUARE
			self.playArea[1][3] = self.SQUARE
			self.playArea[1][4] = self.SQUARE
			self.activePiece = [[0,3], [0,4], [1,3], [1,4]]

			
		if piece == "tPiece":
			self.playArea[1][3] = self.TPIECE
			self.playArea[1][4] = self.TPIECE
			self.playArea[1][5] = self.TPIECE
			self.playArea[0][4] = self.TPIECE
			self.activePiece = [[1,3], [1,4], [1,5], [0,4]]


	
		
	#Takes care of moving the board down one line, this can be called either when the user presses the down key, or as the piece is falling down.
	def lineDown(self):
	
			emptyBelow = True
			self.activePiece.sort()
			self.activePiece.reverse()
			previousValue = self.activePiece[0][0]
			
			#check if none empty block below
			for index, item in enumerate(self.activePiece):
				if(item[0] == previousValue):
					if (item[0]+1) < len(self.playArea) and (self.playArea[(previousValue+1)][item[1]] != self.EMPTY):
						emptyBelow = False
						break
					

			if emptyBelow:
				for index, item in enumerate(self.activePiece):
					temp = []
					temp.append(item[0]+1)
					temp.append(item[1])
					if ((item[0]+1) < len(self.playArea)):
						self.playArea[item[0]+1][item[1]] = self.playArea[item[0]][item[1]]
						self.playArea[item[0]][item[1]] = self.EMPTY
						self.activePiece[index] = temp

					else:
						self.checkForFullLine()
						self.newPiece()
						break
			else:
				self.checkForFullLine()
				self.newPiece()
	
	#Checks for full lines on the board. As soon as it finds a full line, it will pop them and replace with an empty line at the top.
	def checkForFullLine(self):
		popList = []
		fullLine = True
		for index, line in enumerate(self.playArea):
			fullLine = True
			for block in line:
				if(block == self.EMPTY):
					fullLine = False

			if fullLine:
				print "Testing!"
				popList.append(index)
				


			
		if popList:
			print "We are in sir!"
			for item in popList:
				self.playArea.pop(item)
				temp = []
				for col in range(0,self.cols):
					temp.append(self.EMPTY)
				self.playArea.reverse()
				self.playArea.append(temp)
				self.playArea.reverse()
	
	#Handles rotations of the piece. Yet to be implemented.
	def rotatePiece(self, adjustMoveY, adjustMoveX):
		
		#Check if line-piece.
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LINEPIECE:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "flat":
				self.activePiece.sort()
					
				if (self.activePiece[0][1]+1) < self.cols:
					print (self.activePiece[0][1]+1)
							
					#Move first piece
					moveX = 1 + adjustMoveX
					moveY = 1 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + adjustMoveX
					moveY = -1	+ adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = -2 + adjustMoveX
					moveY = -2 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "line"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "line":
				self.activePiece.sort()
						
				if (self.activePiece[0][1]-1) >= 0 and self.activePiece[0][1]+2 < self.cols:
					print (self.activePiece[0][1]+1)
							
					#Move first piece
					moveX = 2 + adjustMoveX
					moveY = 2 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 1 + adjustMoveX
					moveY = 1 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + adjustMoveX
					moveY = 0	+ adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = -1 + adjustMoveX
					moveY = -1 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "flat"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		#Check if L-piece
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LPIECE:
			pass
		#Check if Z-piece	
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.ZPIECE:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "flat":
				self.activePiece.sort()
					
				if (self.activePiece[0][1]+1) < self.cols:
							
					#Move first piece
					moveX = 2 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece ( Not moving as default)
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + adjustMoveX
					moveY = -2 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "standing"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "standing":
				self.activePiece.sort()
				print self.activePiece
				
				if (self.activePiece[0][1]-2) >= 0 and self.activePiece[0][1]-1 >= 0:
					print (self.activePiece[0][1]+1)
							
					#Move first piece
					moveX = -2 + adjustMoveX
					moveY = 1 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + adjustMoveX
					moveY = +1 + adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "flat"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		#Check to see if reverseZ piece.
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.REVERSEZ:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "flat":
				self.activePiece.sort()
					
				if (self.activePiece[1][1]+2) < self.cols:
					#Move first piece
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + adjustMoveX
					moveY = 2 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece
					moveX = 2 + adjustMoveX
					moveY = 0 + adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "standing"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "standing":
				self.activePiece.sort()
				print self.activePiece
				
				if (self.activePiece[0][1]-2) >= 0 and self.activePiece[0][1]-1 >= 0:
					print (self.activePiece[0][1]+1)
							
					#Move first piece
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + adjustMoveX
					moveY = 0 + adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -2 + adjustMoveX
					moveY = 0 + adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + adjustMoveX
					moveY = -2 + adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "flat"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		
		
	#Is invoked whenever the user presses the left-key on the keyboard. This will take care of, you guessed it, moving the piece to the left.	
	def lineLeft(self):
		emptyBlockLeft = True
		self.activePiece.sort(key = itemgetter(1))
		previousValue = self.activePiece[0][0]
		#Check if more than one actice block in same column.
		for index, item in enumerate(self.activePiece):
				
				if (item[1]-1) < 0 :
					emptyBlockLeft = False
					break
				
				else:
					if item[0] != previousValue:
						temp = []
						temp.append(item[0])
						temp.append(item[1]-1)
						if self.playArea[item[0]][item[1]-1] != self.EMPTY and temp not in self.activePiece:							
							emptyBlockLeft = False
							break
						previousValue = item[0]		
		
		if emptyBlockLeft:
			for index, item in enumerate(self.activePiece):
				if((item[1]-1) >= 0 and self.playArea[item[0]][(item[1]-1)] == self.EMPTY):
					temp = []
					temp.append(item[0])
					temp.append(item[1]-1)
					self.playArea[item[0]][(item[1]-1)] = self.playArea[item[0]][item[1]]
					self.playArea[item[0]][item[1]] = self.EMPTY	
					self.activePiece[index] = temp
				else:
					break
	
	#Same as lineLeft, except, right.
	def lineRight(self):
		emptyBlockRight = True
		self.activePiece.sort(key = itemgetter(1))
		self.activePiece.reverse()
		previousValue = self.activePiece[0][0]
		#Check all lines to see if there is a block in the way.
		for index, item in enumerate(self.activePiece):
				
				if (item[1]+1) >= self.cols:
					emptyBlockRight = False
					break
				
				else:
					if item[0] != previousValue:
						temp = []
						temp.append(item[0])
						temp.append(item[1]+1)
						if self.playArea[item[0]][item[1]+1] != self.EMPTY and temp not in self.activePiece:							
							emptyBlockRight = False
							break
						previousValue = item[0]
					
		if emptyBlockRight:
			for index, item in enumerate(self.activePiece):
				if((item[1]+1) < self.cols and self.playArea[item[0]][(item[1]+1)] == self.EMPTY):
					temp = []
					temp.append(item[0])
					temp.append(item[1]+1)
					self.playArea[item[0]][(item[1]+1)] = self.playArea[item[0]][item[1]]
					self.playArea[item[0]][item[1]] = self.EMPTY	
					self.activePiece[index] = temp
				else:
					break
					
	#Randoms a new piece and contacts "addPiece" function. At the moment every piece will be randomed when called, with the same probability.
	def newPiece(self):
		randomedPiece = random.randint(0, 6)
		if randomedPiece == 0:
			self.addPiece("reverseL")
		elif randomedPiece == 1:
			self.addPiece("L")
		elif randomedPiece == 2:
			self.addPiece("linePiece")
		elif randomedPiece == 3:
			self.addPiece("zPiece")
		elif randomedPiece == 4:
			self.addPiece("reverseZ")
		elif randomedPiece == 5:
			self.addPiece("square")
		elif randomedPiece == 6:
			self.addPiece("tPiece")
	
#This class takes care of everything not closely related to the GUI.	
class Main:
	#Initiates the main class.
	def init(self):
		self.running = True
		self.clock = pygame.time.Clock()
		self.GAMEEVENT = USEREVENT +1
		pygame.time.set_timer(self.GAMEEVENT, 750)
		self.gameOver = False
		pygame.mixer.music.load("data\\tetris_theme1.mid")
		pygame.mixer.music.play(-1)
	
	#The main part of the program. The loop which will handle everything from updates to event-handling.
	def loop(self):

			
		while self.running:
			
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
				
				if e.type == self.GAMEEVENT:
					gui.lineDown()
					
				if e.type == KEYDOWN:
					if e.key == K_UP:
						if gui.rotatePiece(0,0):
							pass
						elif gui.rotatePiece(1,1):
							pass
						elif gui.rotatePiece(2,2):
							pass
						elif gui.rotatePiece(-1,-1):
							pass
						
				
			keys = pygame.key.get_pressed()
			if keys[pygame.K_DOWN]:
				gui.lineDown()
			
			if keys[pygame.K_LEFT]:
				gui.lineLeft()
				
			if keys[pygame.K_RIGHT]:
				gui.lineRight()
			
			
			gui.reDraw()
			if self.gameOver:
				gui.screen.blit(gui.gameOverImage, (10,10))
				self.running = False
				
			self.clock.tick(40)
			pygame.display.flip()
				

		
		pygame.quit()

		
gui = GUI()
main = Main()
gui.init()
main.init()
main.loop()
