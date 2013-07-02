#! /usr/bin/env python
import pygame, random
from pygame.locals import *
from Tkinter import *
from operator import itemgetter

class GUI:
	def init(self):
		pygame.init()
		
		
		self.blockEmpty = True
		
		self.EMPTY = "EMPTY"
		self.REVERSEL = pygame.image.load("reverseL24.png")
		self.LPIECE = pygame.image.load("Lblock24.png")
		self.LINEPIECE = pygame.image.load("lineBlock24.png")
		self.ZPIECE = pygame.image.load("zBlock24.png")
		self.REVERSEZ = pygame.image.load("reverseZ24.png")
		self.SQUARE = pygame.image.load("square24.png")
		self.TPIECE = pygame.image.load("tSquare24.png")
		
		
		

		font = pygame.font.SysFont("Arial Black", 90)
		self.gameOverImage = font.render("GAME OVER", True, (255, 0, 0))

		self.background = pygame.image.load("background24.png")
		self.topCover = pygame.image.load("topCover24.png")
		
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

			
		if piece == "reverseZ":
			self.playArea[1][3] = self.REVERSEZ
			self.playArea[1][4] = self.REVERSEZ
			self.playArea[0][4] = self.REVERSEZ
			self.playArea[0][5] = self.REVERSEZ
			self.activePiece = [[1,3], [1,4], [0,4], [0,5]]
			
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
						self.newPiece()
						break
			else:
				self.newPiece()
	def rotatePiece(self):
		print("Hej!")
		print(self.activePiece)
		if self.playArea[self.activePiece[0][0]][self.activePiece[0][1]] == self.LINEPIECE:
			print("Tjena!")
			if self.currentPosition == "flat":
				self.activePiece.sort()
				self.activePiece.reverse()
				
			
		
		
	def lineLeft(self):
		emptyBlockLeft = True
		self.activePiece.sort(key = itemgetter(1))
		previousValue = self.activePiece[0][0]
		#Check if more than one actice block in same column.
		for index, item in enumerate(self.activePiece):
				
				if (item[1]-1) < 0 :
					print "This is smaller!"
					emptyBlockLeft = False
					break
				
				else:
					if item[0] != previousValue:
						temp = []
						temp.append(item[0])
						temp.append(item[1]-1)
						print temp in self.activePiece
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
	
	def lineRight(self):
		emptyBlockRight = True
		self.activePiece.sort(key = itemgetter(1))
		self.activePiece.reverse()
		previousValue = self.activePiece[0][0]
		print self.activePiece
		#Check all lines to see if there is a block in the way.
		for index, item in enumerate(self.activePiece):
				
				if (item[1]+1) >= self.cols:
					print "This is bigger!"
					emptyBlockRight = False
					break
				
				else:
					if item[0] != previousValue:
						temp = []
						temp.append(item[0])
						temp.append(item[1]+1)
						print temp in self.activePiece
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
			
class Main:
	def init(self):
		self.running = True
		self.clock = pygame.time.Clock()
		self.GAMEEVENT = USEREVENT +1
		pygame.time.set_timer(self.GAMEEVENT, 750)
		self.gameOver = False
		
	def loop(self):

			
		while self.running:
			
			for e in pygame.event.get():
				if e.type == QUIT:
					self.running = False
				
				if e.type == self.GAMEEVENT:
					gui.lineDown()
					
				if e.type == KEYDOWN:
					if e.key == K_UP:
						gui.rotatePiece()
				
				
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
			self.clock.tick(40)
			pygame.display.flip()
				

		
		pygame.quit()

		
gui = GUI()
main = Main()
gui.init()
main.init()
main.loop()
