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
		
		self.nextPieces = []
		
		
		
		self.blockEmpty = True
		
		self.EMPTY = "EMPTY"
		self.REVERSEL = pygame.image.load("data\\reverseL24.png")
		self.LPIECE = pygame.image.load("data\\Lblock24.png")
		self.LINEPIECE = pygame.image.load("data\\lineBlock24.png")
		self.ZPIECE = pygame.image.load("data\\zBlock24.png")
		self.REVERSEZ = pygame.image.load("data\\reverseZ24.png")
		self.SQUARE = pygame.image.load("data\\square24.png")
		self.TPIECE = pygame.image.load("data\\tSquare24.png")
		
		self.TPIECEMINI = pygame.image.load("data\\tPieceMini.png")
		self.ZPIECEMINI = pygame.image.load("data\\zPieceMini.png")
		self.REVERSEZMINI = pygame.image.load("data\\reverseZmini.png")
		self.LPIECEMINI = pygame.image.load("data\\LPieceMini.png")
		self.REVERSELMINI = pygame.image.load("data\\reverseLMini.png")
		self.LINEPIECEMINI = pygame.image.load("data\\linePieceMini.png")
		self.SQUAREMINI = pygame.image.load("data\\squarePieceMini.png")		
		

		self.level = 0
		
		
		

		font = pygame.font.SysFont("Arial Black", 50)
		
		self.scoreFont = pygame.font.SysFont("Arial Black", 30)
		
		self.gameOverImage = font.render("GAME OVER", True, (255, 0, 0))

		self.background = pygame.image.load("data\\backgroundExtended.png")
		self.topCover = pygame.image.load("data\\topCover24.png")
		
		self.currentPosition = ""
		self.activePiece = []
		self.playArea = []
		self.lines = 22
		self.cols = 10
		self.piecePushedDown = False
		
		
		self.currentScore = 0
		self.linesCleared = 0
		
		for line in range(0,self.lines):
			temp = []
			for col in range(0,self.cols):
				temp.append(self.EMPTY)
			self.playArea.append(temp)	

		
		
		self.screen = pygame.display.set_mode((440,528), False)
		
		self.screen.blit(self.background, (0,0))
		
		self.newPiece()
		self.newPiece()
		self.newPiece()
		
		self.addPiece()
			
		self.reDraw()
	
	#Scoring found on the following webpage: http://tetris.wikia.com/wiki/Scoring In order to have as authentic feeling as possible.
	def updateScore(self):
		self.score = self.scoreFont.render(str(self.currentScore).rjust(7,"0"), True, (0,255,0))
		self.screen.blit(self.score, (270,150))
		
		self.linesScore = self.scoreFont.render(str(self.linesCleared), True, (0,255,0))
		self.screen.blit(self.linesScore, (330,45))

	
	#Just as the name states this will take of redrawing the board.	
	def reDraw(self):
		self.screen.blit(self.background,(0,0))
		self.updateScore()
		for indexLine, line in enumerate(self.playArea):
			y = indexLine * 24
			for indexCol, item in enumerate(line):
				x = indexCol * 24
				if(item != "EMPTY"):
					self.screen.blit(item, (x,y))
					self.screen.blit(gui.topCover,(0,0))
					
		self.piecesList()
	
		pygame.display.flip()


	#Adds a piece to the board. Will receive a call from the "new piece" function in order to know which piece to add.	
	def addPiece(self):
		if self.nextPieces[0] == self.REVERSELMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.activePiece = []
			self.playArea[0][4] = self.REVERSEL
			self.playArea[1][4] = self.REVERSEL
			self.playArea[1][5] = self.REVERSEL
			self.playArea[1][6] = self.REVERSEL
			self.currentPosition = "up"
			self.activePiece = [[0,4], [1,4], [1,5], [1,6]]
			
		elif self.nextPieces[0] == self.LPIECEMINI:	
			self.nextPieces.pop(0)
			self.newPiece()		
			self.playArea[1][4] = self.LPIECE
			self.playArea[1][5] = self.LPIECE
			self.playArea[1][6] = self.LPIECE
			self.playArea[0][6] = self.LPIECE
			self.activePiece = [[1,4], [1,5], [1,6], [0,6]]
			self.currentPosition = "up"
			
		elif self.nextPieces[0] == self.LINEPIECEMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.playArea[0][3] = self.LINEPIECE
			self.playArea[0][4] = self.LINEPIECE
			self.playArea[0][5] = self.LINEPIECE
			self.playArea[0][6] = self.LINEPIECE
			self.activePiece = [[0,3], [0,4], [0,5], [0,6]]
			self.currentPosition = "flat"
			
		elif self.nextPieces[0] ==  self.ZPIECEMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.playArea[0][3] = self.ZPIECE
			self.playArea[0][4] = self.ZPIECE
			self.playArea[1][4] = self.ZPIECE
			self.playArea[1][5] = self.ZPIECE
			self.activePiece = [[0,3], [0,4], [1,4], [1,5]]
			self.currentPosition = "flat"

			
		elif self.nextPieces[0] == self.REVERSEZMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.playArea[1][3] = self.REVERSEZ
			self.playArea[1][4] = self.REVERSEZ
			self.playArea[0][4] = self.REVERSEZ
			self.playArea[0][5] = self.REVERSEZ
			self.activePiece = [[1,3], [1,4], [0,4], [0,5]]
			self.currentPosition = "flat"
			
		elif self.nextPieces[0] == self.SQUAREMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.playArea[0][3] = self.SQUARE
			self.playArea[0][4] = self.SQUARE
			self.playArea[1][3] = self.SQUARE
			self.playArea[1][4] = self.SQUARE
			self.activePiece = [[0,3], [0,4], [1,3], [1,4]]

			
		elif self.nextPieces[0] ==  self.TPIECEMINI:
			self.nextPieces.pop(0)
			self.newPiece()
			self.playArea[1][3] = self.TPIECE
			self.playArea[1][4] = self.TPIECE
			self.playArea[1][5] = self.TPIECE
			self.playArea[0][4] = self.TPIECE
			self.activePiece = [[1,3], [1,4], [1,5], [0,4]]
			self.currentPosition = "up"

		
	#Takes care of moving the board down one line, this can be called either when the user presses the down key, or as the piece is falling down.
	def lineDown(self):
			
			emptyBelow = True
			self.activePiece.sort()
			self.activePiece.reverse()
			previousValue = self.activePiece[0][0]
			
			for index,item in enumerate(self.activePiece):
				temp = []
				temp.append(item[0]+1)
				temp.append(item[1])
				if (item[0]+1) < len(self.playArea) and (self.playArea[(item[0]+1)][item[1]] != self.EMPTY):
					if temp in self.activePiece:
						continue
					emptyBelow = False
					if (item[0]<2):
						main.gameOver = True
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
						self.addPiece()
						break

						
				if(self.piecePushedDown):
					self.currentScore = self.currentScore + 1
			else:
				self.checkForFullLine()
				self.addPiece()

	
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
				popList.append(index)
				


			
		if popList:
			numberOfLines = len(popList)
			if numberOfLines == 1:
				self.linesCleared = self.linesCleared + 1
				scoreToAdd = 40 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
			elif numberOfLines == 2:
				self.linesCleared = self.linesCleared + 2
				scoreToAdd = 100 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
			elif numberOfLines == 3:
				self.linesCleared = self.linesCleared + 3			
				scoreToAdd = 300 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
			elif numberOfLines == 4:
				self.linesCleared = self.linesCleared + 4
				scoreToAdd = 1200 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
			
			for item in popList:
				self.playArea.pop(item)
				temp = []
				for col in range(0,self.cols):
					temp.append(self.EMPTY)
				self.playArea.reverse()
				self.playArea.append(temp)
				self.playArea.reverse()
	
	#Handles rotations of the piece. Yet to be implemented.
	def rotatePiece(self):
		self.adjustMoveY = 0 
		self.adjustMoveX = 0
		
		#Check if line-piece.
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LINEPIECE:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "flat":
				self.activePiece.sort()
					
				if (self.activePiece[0][1]+1) < self.cols:
							
					#Move first piece
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + self.adjustMoveX
					moveY = -1	+ self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = -2 + self.adjustMoveX
					moveY = -2 + self.adjustMoveY
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
								
					#Move first piece
					moveX = 2 + self.adjustMoveX
					moveY = 2 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0	+ self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = -1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
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
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "up":

				while not allWentWell:

					self.activePiece.sort()
					self.activePiece.reverse()
					
					
						#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = -1 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "right"
					if not allWentWell:
						self.adjustMoveX = self.adjustMoveX + 1
				
			
			elif self.currentPosition == "right":
				self.activePiece.sort()
				if self.activePiece[0][1]-1 >= 0:
							
					#Move first piece
					moveX = -1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "down"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			elif self.currentPosition == "down":
				self.activePiece.sort()

				if (self.activePiece[0][1]) >= 0:
							
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 1 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "left"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell

			elif self.currentPosition == "left":
				self.activePiece.sort()
				if (self.activePiece[1][1]+1) <self.cols:
							
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 1 + self.adjustMoveX
					moveY = -2 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "up"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		
		#Check if reverse-L
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.REVERSEL:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "up":
				self.activePiece.sort()
				
				if (self.activePiece[1][1]+2) < self.cols:
					#Move first piece
					moveX = 1 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "right"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "right":
				self.activePiece.sort()
				if (self.activePiece[0][1]-1) >= 0:
							
					#Move first piece
					moveX = -1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 1 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "down"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "down":
				self.activePiece.sort()
				
				if (self.activePiece[0][1]) >= 0:
							
					#Move first piece
					moveX = 1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = -2 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "left"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell

			if self.currentPosition == "left":
				self.activePiece.sort()
				if (self.activePiece[1][1]+1) <self.cols:
							
					#Move first piece
					moveX = -1 + self.adjustMoveX
					moveY = +1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = -2 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "up"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		
		
		#Check if Z-piece	
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.ZPIECE:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "flat":
				self.activePiece.sort()
					
				if (self.activePiece[0][1]) < self.cols:
							
					#Move first piece
					moveX = 2 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece ( Not moving as default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + self.adjustMoveX
					moveY = -2 + self.adjustMoveY
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
				
				if (self.activePiece[0][1]-2) >= 0:
							
					#Move first piece
					moveX = -2 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = +1 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
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
					
				if (self.activePiece[1][1]) < self.cols:
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 0 + self.adjustMoveX
					moveY = 2 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece
					moveX = 2 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
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
				
				if (self.activePiece[0][1]-1) >= 0:

							
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -2 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + self.adjustMoveX
					moveY = -2 + self.adjustMoveY
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
		
		#Check to to see if T-Piece
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.TPIECE:
			moveX = 0
			moveY = 0
			allWentWell = False
			if self.currentPosition == "up":
				self.activePiece.sort()
				if (self.activePiece[1][1]) < self.cols and (self.activePiece[1][0] +1) < len(self.playArea):
					#Move first piece

					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece ( Not moving as default)
					moveX = 1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					
					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "right"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
		
			if self.currentPosition == "right":
				self.activePiece.sort()
				if (self.activePiece[0][1]-1) >= 0:
							
					#Move first piece
					moveX = -1 + self.adjustMoveX
					moveY = 1 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "down"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell
			
			
			if self.currentPosition == "down":
				self.activePiece.sort()
				
				if (self.activePiece[0][1]) >= 0:
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = -1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "left"
					return allWentWell
				
				else:
					allWentWell = False
					return allWentWell

			if self.currentPosition == "left":
				self.activePiece.sort()
				if (self.activePiece[3][1]+1) <self.cols:
							
					#Move first piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
						self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
						self.activePiece[0][0] = self.activePiece[0][0] + moveY
						self.activePiece[0][1] = self.activePiece[0][1] + moveX
					
					#Move second piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY
					if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
						self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
						self.activePiece[1][0] = self.activePiece[1][0] + moveY
						self.activePiece[1][1] = self.activePiece[1][1] + moveX

					#Move third piece
					moveX = 0 + self.adjustMoveX
					moveY = 0 + self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
						self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
						self.activePiece[2][0] = self.activePiece[2][0] + moveY
						self.activePiece[2][1] = self.activePiece[2][1] + moveX
						
					#Move fourth piece (not moving per default)
					moveX = 1 + self.adjustMoveX
					moveY = -1 + self.adjustMoveY
					if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
						self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
						self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
						self.activePiece[3][0] = self.activePiece[3][0] + moveY
						self.activePiece[3][1] = self.activePiece[3][1] + moveX				
					allWentWell = True
					self.currentPosition = "up"
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
			self.nextPieces.append(self.REVERSELMINI)
			# self.addPiece("reverseL")
		elif randomedPiece == 1:
			self.nextPieces.append(self.LPIECEMINI)
			# self.addPiece("L")
		elif randomedPiece == 2:
			self.nextPieces.append(self.LINEPIECEMINI)
			# self.addPiece("linePiece")
		elif randomedPiece == 3:
			self.nextPieces.append(self.ZPIECEMINI)
			# self.addPiece("zPiece")
		elif randomedPiece == 4:
			self.nextPieces.append(self.REVERSEZMINI)
			# self.addPiece("reverseZ")
		elif randomedPiece == 5:
			self.nextPieces.append(self.SQUAREMINI)
			# self.addPiece("square")
		elif randomedPiece == 6:
			self.nextPieces.append(self.TPIECEMINI)
			# self.addPiece("tPiece")
			

	
	#Handles display of the coming pieces
	def piecesList(self):
		for index, item in enumerate(self.nextPieces):
			self.screen.blit(item, (310,((index + 1) * 80 + 180)))
		
		
	
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
			
				if e.type == KEYUP:
					if e.key == K_DOWN:
						gui.piecePushedDown = False
			
				if e.type == KEYDOWN:
					if e.key == K_UP:
						gui.rotatePiece()
					if e.key == K_LEFT:
						gui.lineLeft()
					if e.key == K_RIGHT:
						gui.lineRight()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_DOWN]:
				gui.piecePushedDown = True
				gui.lineDown()
				gui.piecePushedDown = False
			
			if keys[pygame.K_LEFT]:
				pass
				
			if keys[pygame.K_RIGHT]:
				pass
			
			
			
			if self.gameOver:
				gui.screen.blit(gui.gameOverImage, (45,60))
			
			else:
				gui.reDraw()
				
			self.clock.tick(40)
			pygame.display.flip()
				


		pygame.quit()


		
gui = GUI()
main = Main()
gui.init()
main.init()
main.loop()
