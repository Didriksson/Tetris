#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Program created by mattias Didriksson as a project in "Multimediaprogrammering i Python".
OS: Windows 7
Pythonversion: 2.7.5

This is a simple Tetris clone, made from scratch by me. 

"""


import pygame, random, os.path, HandleData_module
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

#The GUI class responsible for most of the program. Reason for that is because the GUI is such a central part of a program like Tetris.
class GUI:
	#A function which will initiate the class. I.e. set up windows, initiate attributes etc.
	def init(self, sentScreen, grid, soundOption):
		pygame.init()
		
		self.sound = soundOption
		self.screen = sentScreen
		self.screen.fill((0,0,0))
		
		
		self.fromInstant = False
		
		self.nextPieces = []
		
		#Sound effects mainly generated from http://www.bfxr.net/
		self.tetrisSound = pygame.mixer.Sound(os.path.join('data','tetrisFX.wav'))
		self.lineSound = pygame.mixer.Sound(os.path.join('data','lineFX.wav'))
		
		
		self.playAgainMarked = True
		
		self.blockEmpty = True
		
		self.fadeToBlack = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
		self.fadeToBlack.convert()
		self.fadeToBlack.fill((0,0,0))
		self.fadeToBlack.set_alpha(100)

		
		if grid:
			self.REVERSEL = pygame.image.load(os.path.join('data/Grid','reverseL24.png'))
			self.LPIECE = pygame.image.load(os.path.join('data/Grid','LBlock24.png'))
			self.LINEPIECE = pygame.image.load(os.path.join('data/Grid','lineBlock24.png'))
			self.ZPIECE = pygame.image.load(os.path.join('data/Grid','zBlock24.png'))
			self.REVERSEZ = pygame.image.load(os.path.join('data/Grid','reverseZ24.png'))
			self.SQUARE = pygame.image.load(os.path.join('data/Grid','square24.png'))
			self.TPIECE = pygame.image.load(os.path.join('data/Grid','tSquare24.png'))
			self.background = pygame.image.load(os.path.join('data/Grid','backgroundExtended.png'))			
		else:
			self.REVERSEL = pygame.image.load(os.path.join('data/NoGrid','reverseL24.png'))
			self.LPIECE = pygame.image.load(os.path.join('data/NoGrid','LBlock24.png'))
			self.LINEPIECE = pygame.image.load(os.path.join('data/NoGrid','lineBlock24.png'))
			self.ZPIECE = pygame.image.load(os.path.join('data/NoGrid','zBlock24.png'))
			self.REVERSEZ = pygame.image.load(os.path.join('data/NoGrid','reverseZ24.png'))
			self.SQUARE = pygame.image.load(os.path.join('data/NoGrid','square24.png'))
			self.TPIECE = pygame.image.load(os.path.join('data/NoGrid','tSquare24.png'))
			self.background = pygame.image.load(os.path.join('data/NoGrid','backgroundExtended.png'))
		
		self.EMPTY = "EMPTY"
		
		self.TPIECEMINI = pygame.image.load(os.path.join('data','tPieceMini.png'))
		self.ZPIECEMINI = pygame.image.load(os.path.join('data','zPieceMini.png'))
		self.REVERSEZMINI = pygame.image.load(os.path.join('data','reverseZmini.png'))
		self.LPIECEMINI = pygame.image.load(os.path.join('data','LPieceMini.png'))
		self.REVERSELMINI = pygame.image.load(os.path.join('data','reverseLMini.png'))
		self.LINEPIECEMINI = pygame.image.load(os.path.join('data','linePieceMini.png'))
		self.SQUAREMINI = pygame.image.load(os.path.join('data','squarePieceMini.png'))		
		
		self.playAgainMenuImage = pygame.image.load(os.path.join('data','playAgainMenu.png'))
		self.playAgainMenuButton = pygame.image.load(os.path.join('data','playAgainButton.png'))
		self.playAgainMenuButtonMarked = pygame.image.load(os.path.join('data','playAgainButtonMarked.png'))


		self.topCover = pygame.image.load(os.path.join('data','topCover24.png'))
		
		self.highscorePopUpImage = pygame.image.load(os.path.join('data', 'highscorePopUp.png'))
		
		
		self.level = 0
		
		
		

		self.gameOverFont = pygame.font.SysFont("Arial Black", 50)
		self.scoreFont = pygame.font.SysFont("Arial Black", 30)
		self.levelFont = pygame.font.SysFont("Arial Black", 20)	
		self.scoreTextFont = pygame.font.SysFont("Arial Black", 25)
		self.playAgainMenuFont = pygame.font.SysFont("SKETCHFLOW PRINT", 20)
		self.enterNameFont = pygame.font.SysFont("Arial Black", 15)
		
		

		self.gameOverImage = self.gameOverFont.render("GAME OVER", True, (255, 0, 0))
		self.gamePausedText = self.gameOverFont.render("PAUSED", True, (255, 0, 0))
		self.scoreText = self.scoreTextFont.render("SCORE: ", True, (255,255,255))
		self.linesText = self.levelFont.render("LINES: ", True, (255,255,255))
		self.levelText = self.levelFont.render("LEVEL: ", True, (255,255,255))
		self.playAgainTextYes = self.playAgainMenuFont.render("YES", True, (255,255,255))
		self.playAgainTextNo = self.playAgainMenuFont.render("NO", True, (255, 255, 255))
		self.playAgainText = self.playAgainMenuFont.render("Do you want to play again?", True, (255,255,255))
		self.confirmExitText = self.playAgainMenuFont.render("Do you really want to quit?", True, (255,255,255))
		
		
		self.playerName = ""
		self.currentPosition = ""
		self.activePiece = []
		self.playArea = []
		self.lines = 22
		self.cols = 10
		self.piecePushedDown = False
		self.madeHighScore = False
		
		
		self.currentScore = 0
		self.linesCleared = 0
		
		for line in range(0,self.lines):
			temp = []
			for col in range(0,self.cols):
				temp.append(self.EMPTY)
			self.playArea.append(temp)	

		
		
		self.screen.blit(self.background, (24,0))
		
		self.newPiece()
		self.newPiece()
		self.newPiece()
		
		self.addPiece()
			
		self.reDraw()
	
	#Scoring found on the following webpage: http://tetris.wikia.com/wiki/Scoring In order to have as authentic feeling as possible.
	def updateScore(self):
		
		
		self.displayLevel = self.scoreFont.render(str(self.level).rjust(2,"0"), True, (255,255,255))
		self.screen.blit(self.displayLevel, (387, 43))
		
		self.screen.blit(self.levelText, (294, 50))
		
		self.screen.blit(self.scoreText, (314,140))
		
		self.score = self.scoreFont.render(str(self.currentScore).rjust(7,"0"), True, (255,255,255))
		self.screen.blit(self.score, (294,175))
		
		self.linesScore = self.scoreFont.render(str(self.linesCleared).rjust(3,"0"), True, (255,255,255))
		self.screen.blit(self.linesScore, (378,90))
		self.screen.blit(self.linesText, ( 294, 98))
	
	#Just as the name states this will take of redrawing the board.	
	def reDraw(self):
		self.screen.blit(self.background,(24,0))
		self.updateScore()
		for indexLine, line in enumerate(self.playArea):
			y = indexLine * 24
			for indexCol, item in enumerate(line):
				x = indexCol * 24 + 24
				if(item != "EMPTY"):
					self.screen.blit(item, (x,y))
					self.screen.blit(gui.topCover,(24,0))
					
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
			
			self.instantPossible = True
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
						self.instantPossible = False
						self.addPiece()
						break

						
				if self.piecePushedDown or self.fromInstant:
					self.currentScore = self.currentScore + 1
					self.fromInstant = False
					
				
				return self.instantPossible
			else:
				self.checkForFullLine()
				self.addPiece()
				self.instantPossible = False
				return self.instantPossible
	
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
				if self.sound:
					self.lineSound.play()
			elif numberOfLines == 2:
				self.linesCleared = self.linesCleared + 2
				scoreToAdd = 100 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
				if self.sound:
					self.lineSound.play()
			elif numberOfLines == 3:
				self.linesCleared = self.linesCleared + 3			
				scoreToAdd = 300 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
				if self.sound:
					self.lineSound.play()
			elif numberOfLines == 4:
				self.linesCleared = self.linesCleared + 4
				scoreToAdd = 1200 * (self.level + 1)
				self.currentScore = self.currentScore + scoreToAdd
				if self.sound:
					self.tetrisSound.play()
			for item in popList:
				self.playArea.pop(item)
				temp = []
				for col in range(0,self.cols):
					temp.append(self.EMPTY)
				self.playArea.reverse()
				self.playArea.append(temp)
				self.playArea.reverse()
			

			if(self.linesCleared >= ((self.level * 10) + 10)):
				self.levelUp()
				
	def rotateCheckAndMove(self, moveX1, moveY1, moveX2, moveY2, moveX3, moveY3, moveX4, moveY4):
		
			moveX = moveX1 + self.adjustMoveX
			moveY = moveY1 + self.adjustMoveY
			if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY or [(self.activePiece[0][0] + moveY),(self.activePiece[0][1] +moveX)] in self.activePiece:
				moveX = moveX2 + self.adjustMoveX
				moveY = moveY2 + self.adjustMoveY										
				if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY or [(self.activePiece[1][0] + moveY),(self.activePiece[1][1] +moveX)] in self.activePiece:
					moveX = moveX3 + self.adjustMoveX
					moveY = moveY3	+ self.adjustMoveY			
					if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY or [(self.activePiece[2][0] + moveY),(self.activePiece[2][1] +moveX)] in self.activePiece:
						moveX = moveX4 + self.adjustMoveX
						moveY = moveY4 + self.adjustMoveY
						if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY or [(self.activePiece[3][0] + moveY),(self.activePiece[3][1] +moveX)] in self.activePiece:
							#Move first piece
							moveX = moveX1 + self.adjustMoveX
							moveY = moveY1 + self.adjustMoveY
							if self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] == self.EMPTY:
								self.playArea[(self.activePiece[0][0]) + moveY][(self.activePiece[0][1]) +moveX] = self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])]
								self.playArea[(self.activePiece[0][0])][(self.activePiece[0][1])] = self.EMPTY
								self.activePiece[0][0] = self.activePiece[0][0] + moveY
								self.activePiece[0][1] = self.activePiece[0][1] + moveX
							
							#Move second piece ( Not moving as default)
							moveX = moveX2 + self.adjustMoveX
							moveY = moveY2 + self.adjustMoveY
							if self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] == self.EMPTY:
								self.playArea[(self.activePiece[1][0]) + moveY][(self.activePiece[1][1]) +moveX] = self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])]
								self.playArea[(self.activePiece[1][0])][(self.activePiece[1][1])] = self.EMPTY
								self.activePiece[1][0] = self.activePiece[1][0] + moveY
								self.activePiece[1][1] = self.activePiece[1][1] + moveX

							#Move third piece
							moveX = moveX3 + self.adjustMoveX
							moveY = moveY3	+ self.adjustMoveY			
							if self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] == self.EMPTY:
								self.playArea[(self.activePiece[2][0]) + moveY][(self.activePiece[2][1]) +moveX] = self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])]
								self.playArea[(self.activePiece[2][0])][(self.activePiece[2][1])] = self.EMPTY
								self.activePiece[2][0] = self.activePiece[2][0] + moveY
								self.activePiece[2][1] = self.activePiece[2][1] + moveX
								
							#Move fourth piece
							moveX = moveX4 + self.adjustMoveX
							moveY = moveY4 + self.adjustMoveY
							if self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] == self.EMPTY:
								self.playArea[(self.activePiece[3][0]) + moveY][(self.activePiece[3][1]) +moveX] = self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])]
								self.playArea[(self.activePiece[3][0])][(self.activePiece[3][1])] = self.EMPTY
								self.activePiece[3][0] = self.activePiece[3][0] + moveY
								self.activePiece[3][1] = self.activePiece[3][1] + moveX				
							allWentWell = True
							return allWentWell
	
	#Handles rotations of the piece.
	def rotatePiece(self,rotateDirection):
		self.adjustMoveY = 0 
		self.adjustMoveX = 0
		
		#Check if line-piece.
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LINEPIECE:

				allWentWell = False
				if self.currentPosition == "flat":
					self.activePiece.sort()
					if (self.activePiece[0][1]+1) < self.cols and not self.activePiece[0][0] <2:
						allWentWell = self.rotateCheckAndMove(1,1,0,0,-1,-1,-2,-2)
						self.currentPosition = "line"
						return allWentWell
					else:
						allWentWell = False
						return allWentWell
				

				
				if self.currentPosition == "line":
					self.activePiece.sort()
							
					if (self.activePiece[0][1]-1) >= 0 and self.activePiece[0][1]+2 < self.cols:
						allWentWell = self.rotateCheckAndMove(2,2,1,1,0,0,-1,-1)
						self.currentPosition = "flat"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
		#Check if L-piece
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LPIECE:
			if rotateDirection == "RIGHT":
				moveX = 0
				moveY = 0
				allWentWell = False
				if self.currentPosition == "up":


					self.activePiece.sort()
					self.activePiece.reverse()
					allWentWell = self.rotateCheckAndMove(0,1,0,0,1,1,-1,0)
					self.currentPosition = "right"
					return allWentWell

				elif self.currentPosition == "right":
					self.activePiece.sort()
					if self.activePiece[0][1]-1 >= 0:

						allWentWell = self.rotateCheckAndMove(-1,1,0,0,-1,0,0,-1)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				elif self.currentPosition == "down":
					self.activePiece.sort()

					if (self.activePiece[0][1]) >= 0:
										
						allWentWell = self.rotateCheckAndMove(0,-1,0,0,-1,-1,1,0)
						self.currentPosition = "left"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				elif self.currentPosition == "left":
					self.activePiece.sort()
					if (self.activePiece[1][1]+1) <self.cols:
			
						allWentWell = self.rotateCheckAndMove(0,1,1,1,0,0,1,-2)
						self.currentPosition = "up"
						return allWentWell
			
					else:
						allWentWell = False
						return allWentWell
			
			
			#Checking rotating direction.
			if rotateDirection == "LEFT":
				moveX = 0
				moveY = 0
				allWentWell = False
				if self.currentPosition == "up":

					self.activePiece.sort()
					self.activePiece.reverse()
					allWentWell = self.rotateCheckAndMove(-1,-1,0,0,1,1,-2,0)
					self.currentPosition = "left"
					return allWentWell
					
				elif self.currentPosition == "left":
					self.activePiece.sort()
					if self.activePiece[0][1]-1 >= 0:
			
						allWentWell = self.rotateCheckAndMove(0,1,-1,2,0,0,1,-1)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				elif self.currentPosition == "down":
					self.activePiece.sort()
					if (self.activePiece[0][1]) >= 0:
						allWentWell = self.rotateCheckAndMove(1,1,0,0,-1,-1,2,0)
						self.currentPosition = "right"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				elif self.currentPosition == "right":
					self.activePiece.sort()
					if (self.activePiece[1][1]+1) <self.cols:
						allWentWell = self.rotateCheckAndMove(1,0,0,0,-1,-1,0,-1)
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
			if rotateDirection == "RIGHT":

				if self.currentPosition == "up":
					self.activePiece.sort()
					
					if (self.activePiece[1][1]+2) < self.cols:
		
						allWentWell = self.rotateCheckAndMove(1,0,1,1,0,0,0,-1)
						self.currentPosition = "right"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "right":
					self.activePiece.sort()
					if (self.activePiece[0][1]-1) >= 0:
						allWentWell = self.rotateCheckAndMove(-1,1,0,1,0,0,1,0)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "down":
					self.activePiece.sort()
					
					if (self.activePiece[0][1]) >= 0:
						allWentWell = self.rotateCheckAndMove(1,-1,0,0,-1,1,-2,0)
						self.currentPosition = "left"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				if self.currentPosition == "left":
					self.activePiece.sort()
					if (self.activePiece[1][1]+1) <self.cols:
						allWentWell = self.rotateCheckAndMove(-1,1,0,0,0,-2,1,-1)
						self.currentPosition = "up"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
		
			if rotateDirection == "LEFT":

				if self.currentPosition == "up":
					self.activePiece.sort()
					if (self.activePiece[1][1]+2) < self.cols:
						allWentWell = self.rotateCheckAndMove(1,0,0,1,0,0,-1,1)
						self.currentPosition = "left"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "left":
					self.activePiece.sort()

					if (self.activePiece[0][1]-1) >= 0:
						allWentWell = self.rotateCheckAndMove(-1,1,0,0,2,0,1,-1)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "down":
					self.activePiece.sort()
					if (self.activePiece[0][1]) >= 0:
						allWentWell = self.rotateCheckAndMove(1,-1,0,0,0,-1,-1,0)
						self.currentPosition = "right"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				if self.currentPosition == "right":
					self.activePiece.sort()

					if (self.activePiece[1][1]+1) <self.cols:
						allWentWell = self.rotateCheckAndMove(-1,0,0,1,0,0,-1,-1)
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
						allWentWell = self.rotateCheckAndMove(2,0,0,0,0,0,0,-2)
						self.currentPosition = "standing"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "standing":
					self.activePiece.sort()
					
					if (self.activePiece[0][1]-2) >= 0:
						allWentWell = self.rotateCheckAndMove(-2,1,0,0,0,1,0,0)
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
						allWentWell = self.rotateCheckAndMove(0,0,0,2,2,0,0,0)
						self.currentPosition = "standing"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "standing":
					self.activePiece.sort()
					
					if (self.activePiece[0][1]-1) >= 0:
										allWentWell = self.rotateCheckAndMove(0,0,0,0,-2,0,0,-2)
										self.currentPosition = "flat"
										return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
		#Check to to see if T-Piece
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.TPIECE:
			if rotateDirection == "RIGHT":
				moveX = 0
				moveY = 0
				allWentWell = False
				if self.currentPosition == "up":
					self.activePiece.sort()
					if (self.activePiece[1][1]) < self.cols and (self.activePiece[1][0] +1) < len(self.playArea):
						allWentWell = self.rotateCheckAndMove(0,0,1,1,0,0,0,0)
						self.currentPosition = "right"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
			
				if self.currentPosition == "right":
					self.activePiece.sort()
					if (self.activePiece[0][1]-1) >= 0:
						allWentWell = self.rotateCheckAndMove(-1,1,0,0,0,0,0,0)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "down":
					self.activePiece.sort()
					
					if (self.activePiece[0][1]) >= 0:
						allWentWell = self.rotateCheckAndMove(0,0,0,0,-1,-1,0,0)
						self.currentPosition = "left"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				if self.currentPosition == "left":
					self.activePiece.sort()
					if (self.activePiece[3][1]+1) <self.cols:
						allWentWell = self.rotateCheckAndMove(0,0,0,0,0,0,1,-1)
						self.currentPosition = "up"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
		
		
			if rotateDirection == "LEFT":
				moveX = 0
				moveY = 0
				allWentWell = False
				if self.currentPosition == "up":
					self.activePiece.sort()
					if (self.activePiece[1][1]) < self.cols and (self.activePiece[1][0] +1) < len(self.playArea):
						allWentWell = self.rotateCheckAndMove(0,0,0,0,0,0,-1,1)
						self.currentPosition = "left"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
			
				if self.currentPosition == "left":
					self.activePiece.sort()
					if (self.activePiece[0][1]-1) >= 0:
						allWentWell = self.rotateCheckAndMove(1,1,0,0,0,0,0,0)
						self.currentPosition = "down"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell
				
				
				if self.currentPosition == "down":
					self.activePiece.sort()
					if (self.activePiece[0][1]) >= 0:
						allWentWell = self.rotateCheckAndMove(1,-1,0,0,0,0,0,0)
						self.currentPosition = "right"
						return allWentWell
					
					else:
						allWentWell = False
						return allWentWell

				if self.currentPosition == "right":
					self.activePiece.sort()
					if (self.activePiece[3][1]+1) <self.cols:
						allWentWell = self.rotateCheckAndMove(0,0,0,0,0,0,-1,-1)
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

		elif randomedPiece == 1:
			self.nextPieces.append(self.LPIECEMINI)

		elif randomedPiece == 2:
			self.nextPieces.append(self.LINEPIECEMINI)

		elif randomedPiece == 3:
			self.nextPieces.append(self.ZPIECEMINI)

		elif randomedPiece == 4:
			self.nextPieces.append(self.REVERSEZMINI)

		elif randomedPiece == 5:
			self.nextPieces.append(self.SQUAREMINI)
		
		elif randomedPiece == 6:
			self.nextPieces.append(self.TPIECEMINI)
			
	def levelUp(self):
		self.level = self.level + 1
		main.speedDown = int((main.speedDown * 0.85)) 
		pygame.time.set_timer(main.LINEDOWNEVENT, main.speedDown)
	
	#Handles display of the coming pieces
	def piecesList(self):
		for index, item in enumerate(self.nextPieces):
			self.screen.blit(item, (334,((index + 1) * 80 + 180)))
		
	#Displaying a pop up window for entering players name, this only happens if player is within the top 20. Input box have been inspired from
	#http://www.pygame.org/pcr/inputbox/
	def highscorePopUpWindow(self):
		enteredName = False
		tempString = ""
		
		while not enteredName:
			self.screen.blit(self.highscorePopUpImage, (70,200))
			self.enterNameText = self.enterNameFont.render(tempString.upper(), True, (0, 0, 0))
			self.screen.blit(self.enterNameText, (170,254))
			for e in pygame.event.get():
				if e.type == KEYDOWN:
					if e.key == K_RETURN:
						self.playerName = tempString.upper()
						enteredName = True
					elif e.key == K_BACKSPACE:
						if tempString:
							tempString = tempString[:-1]
					
					elif e.key <= 127:
							if len(tempString) < 18:
								tempString = tempString + chr(e.key)
													
			main.clock.tick(40)
			pygame.display.flip()

			
		main.highscoreList.append((self.playerName, self.currentScore))
		if len(main.highscoreList) >= 19:
			main.highscoreList.sort(key = itemgetter(1))
			main.highscoreList.reverse()
			main.highscoreList.pop()
				
		if main.highscoreList:
			data.writeData(main.highscoreList)
			
	def playAgainMenu(self):
		self.screen.blit(self.playAgainMenuImage, (70,200))
		self.screen.blit(self.playAgainText, (80,225))
		if self.playAgainMarked:
			self.screen.blit(self.playAgainMenuButton, (105,260))
			self.screen.blit(self.playAgainMenuButtonMarked, (225,260))
		else:
			self.screen.blit(self.playAgainMenuButtonMarked, (105,260))
			self.screen.blit(self.playAgainMenuButton, (225,260))
		self.screen.blit(self.playAgainTextYes, ( 135, 263))
		self.screen.blit(self.playAgainTextNo, ( 263, 263))	

	def instantDown(self):
		for i in range(20):
			self.fromInstant = True
			if not self.lineDown():
				break
		
#This class takes care of everything not closely related to the GUI.	
class Main:
	#Initiates the main class.
	def init(self,sound):
		self.running = True
		self.clock = pygame.time.Clock()
		self.LINEDOWNEVENT = USEREVENT +1
		self.MOVEXEVENT = USEREVENT +2
		self.speedDown = 750
		pygame.time.set_timer(self.LINEDOWNEVENT, self.speedDown)
		pygame.time.set_timer(self.MOVEXEVENT, 240)
		

		self.gameOver = False
		self.paused = False
		self.moveRight = False
		self.moveLeft = False
		self.exitMenu = False
		self.firstMoveX = True
		
		self.highscoreList = data.readData()
		self.highscoreList.sort(key = itemgetter(1))
		self.highscoreList.reverse()
		
		#http://home.swipnet.se/~w-22134/nmm/mitten.html
		
		pygame.mixer.music.load(os.path.join('data','Tetristheme.ogg'))
		if sound:
			pygame.mixer.music.play(-1)

		
	#The main part of the program. The loop which will handle everything from updates to event-handling.
	def loop(self):

		self.returnValue = ""	
		while self.running:
			if not self.gameOver:
				if not self.paused and not self.exitMenu:
					for e in pygame.event.get():

						if e.type == QUIT:
								self.running = False
								self.returnValue = "QUIT"
						
						if e.type == self.LINEDOWNEVENT:
							gui.lineDown()
							
						if e.type == self.MOVEXEVENT:
							if self.moveRight:
								if 	not self.firstMoveX:
									gui.lineRight()
								else:
									self.firstMoveX = False
									
							elif self.moveLeft:
								if 	not self.firstMoveX:
									gui.lineLeft()
								else:
									self.firstMoveX = False
							
						if e.type == KEYUP:
							if e.key == K_DOWN:
								gui.piecePushedDown = False
					
						if e.type == KEYDOWN:
							if e.key == K_UP:
								gui.rotatePiece("RIGHT")
							if e.key == K_LEFT:
								gui.lineLeft()
								self.firstMoveX = True
							if e.key == K_RIGHT:
								gui.lineRight()
								self.firstMoveX = True
								
							if e.key == K_x:
								gui.rotatePiece("RIGHT")
							if e.key == K_z:
								gui.rotatePiece("LEFT")
							if e.key == K_SPACE:
								gui.instantDown()
							if e.key == K_ESCAPE:
								self.exitMenu = True
								pygame.mixer.music.pause()
							if e.key == K_p:
								self.paused = True
								pygame.mixer.music.pause()
								
					keys = pygame.key.get_pressed()
					if keys[pygame.K_DOWN]:
						gui.piecePushedDown = True
						gui.lineDown()
						gui.piecePushedDown = False

					if keys[pygame.K_LEFT]:
						self.moveLeft = True

					else:
						self.moveLeft = False

					if keys[pygame.K_RIGHT]:
						self.moveRight = True
					else:
						self.moveRight = False
					if self.gameOver:
						gui.screen.blit(gui.fadeToBlack,(0,0))
						gui.screen.blit(gui.gameOverImage, (70,60))

					else:
						gui.reDraw()					

					self.clock.tick(40)
					pygame.display.flip()
					
				else:
					gui.screen.blit(gui.fadeToBlack,(0,0))
					if self.paused:
						gui.screen.blit(gui.gamePausedText,(140,150))
						while self.paused:
							self.clock.tick(40)
							pygame.display.flip()

							for e in pygame.event.get():
							
								if e.type == QUIT:
									self.running = False
									self.returnValue = "QUIT"
									self.paused = False
									pygame.mixer.music.unpause()
								if e.type == KEYDOWN:
									if e.key == K_ESCAPE:
										self.paused = False
										pygame.mixer.music.unpause()
									if e.key == K_p:
										pygame.mixer.music.unpause()
										self.paused = False
										
										
					if self.exitMenu:
						resume = True
						while self.exitMenu:
							gui.screen.blit(gui.playAgainMenuImage, (70,200))
							gui.screen.blit(gui.confirmExitText, (80,225))
							if resume:
								gui.screen.blit(gui.playAgainMenuButton, (105,260))
								gui.screen.blit(gui.playAgainMenuButtonMarked, (225,260))
								gui.screen.blit(gui.playAgainTextYes, ( 135, 263))
								gui.screen.blit(gui.playAgainTextNo, ( 263, 263))	
							else:
								gui.screen.blit(gui.playAgainMenuButtonMarked, (105,260))
								gui.screen.blit(gui.playAgainMenuButton, (225,260))
								gui.screen.blit(gui.playAgainTextYes, ( 135, 263))
								gui.screen.blit(gui.playAgainTextNo, ( 263, 263))	

							self.clock.tick(40)
							pygame.display.flip()

							for e in pygame.event.get():
							
								if e.type == QUIT:
									self.running = False
									self.returnValue = "QUIT"
									self.exitMenu = False
								if e.type == KEYDOWN:
									if e.key == K_ESCAPE:
										self.exitMenu = False
										pygame.mixer.music.unpause()

									if e.key == K_LEFT:
										resume = False
									if e.key == K_RIGHT:
										resume = True
									if e.key == K_RETURN:
										if resume:
											self.exitMenu = False
											pygame.mixer.music.unpause()
										else:
											self.exitMenu = False
											self.running = False
											pygame.mixer.music.stop()

										
			else:
				pygame.mixer.music.stop()
				if len(self.highscoreList) <20:
					gui.madeHighScore = True
				else:
					for item in self.highscoreList:
						if gui.currentScore > item[1]:
							gui.madeHighScore = True
							break
						
				if gui.madeHighScore:
					gui.highscorePopUpWindow()
				self.optionPicked = False
				while not self.optionPicked:
					for e in pygame.event.get():
						if e.type == KEYDOWN:
							if e.key == K_LEFT:
								gui.playAgainMarked = True
							if e.key == K_RIGHT:
								gui.playAgainMarked = False
							if e.key == K_RETURN:
								if gui.playAgainMarked:
									self.returnValue = "AGAIN"
									self.optionPicked = True
								else:
									self.returnValue = "MENU"
									self.optionPicked = True
					gui.playAgainMenu()
					self.clock.tick(40)
					pygame.display.flip()
				
				return self.returnValue
				
		return self.returnValue

		
def start(screen, grid, sound):
	main.init(sound)
	gui.init(screen, grid, sound)
	shouldQuit = main.loop()
	return shouldQuit
	 

gui = GUI()
main = Main()
data = HandleData_module.HandleData()