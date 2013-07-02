import pygame
from pygame.locals import *

def main():

	

	luigi_x = 50
	luigi_y = 50
	pygame.init()
	
	screen = pygame.display.set_mode((800,600))
	background = pygame.image.load('bg.png')
	font = pygame.font.SysFont('Arial Black', 90)
	gameOverImage = font.render("GAME OVER", True, (255,0,0))
	luigi = pygame.image.load('luigi.png')

	
	screen.blit(background, (0,0))
	screen.blit(luigi, (luigi_x,luigi_y), (25,0, 20,25))
	screen.blit(gameOverImage, (100,50))

	clock = pygame.time.Clock()
	
	pygame.display.flip()
	
	running = True
	while running:
		for e in pygame.event.get():
			if e.type == QUIT:
				running = False
			
			if e.type == KEYDOWN:
				if e.key == K_DOWN:
					luigi_x += 10

				if e.key == K_UP:
					luigi_y += 10
					
					
		pygame.display.flip()
		clock.tick(30)
	pygame.quit()

main()