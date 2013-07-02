import pygame
from pygame.locals import *
import Box2D # The main library
from Box2D.b2 import * # This maps Box2D.b2Vec2 to vec2 (and so on)


world=world(gravity=(0,0),doSleep=True)


# Create a dynamic body
dynamic_body=world.CreateDynamicBody(position=(10,15), angle=15)

# And add a box fixture onto it (with a nonzero density, so it will move)
box=dynamic_body.CreatePolygonFixture(box=(2,1), density=1, friction=0.3)

screen = pygame.display.set_mode((640, 400), 0, 32)
clock = pygame.time.Clock()
pygame.init()
luigiX = 50
luigiY = 1
running = True
turnLeft = False
turnRight = False
forAcc = False
backAcc = False
speedX = 0

luigi = pygame.image.load('luigi.png')
screen.blit(luigi,( luigiX, luigiY))

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				turnRight = True
			if event.key == K_LEFT:
				turnLeft = True
			if event.key == K_UP:
				forAcc = True
			if event.key == K_DOWN:
				backAcc = True
				
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				turnRight = False
			if event.key == K_LEFT:
				turnLeft = False
			if event.key == K_UP:
				forAcc = False
			if event.key == K_DOWN:
				backAcc = False
	
	if(turnRight):
		dynamic_body.ApplyTorque(50.0, True)
		print("Right!")
	if(turnLeft):
		dynamic_body.ApplyTorque(-50.0, True)
		print("Left!")
	if(forAcc):
		#speedY = 100
		f = dynamic_body.GetWorldVector(localVector=(0.0, -200.0))
		p = dynamic_body.GetWorldPoint(localPoint=(0.0, 2.0))
		dynamic_body.ApplyForce(f,p,True)
	
	if(backAcc):
		speedY = -100
		dynamic_body.ApplyForce(force = (0,speedY), point = dynamic_body.worldCenter, wake = True)
	
	
	screen.fill((0,0,0,0))
	luigiY = 400 - dynamic_body.position.y * 20
	luigiX = dynamic_body.position.x * 20
	screen.blit(luigi,( luigiX, luigiY), (25,0, 20,25))
	pygame.display.flip()
	clock.tick(30)
	world.Step(1.0/60.0  , 10 , 10 )

	
	
pygame.quit()