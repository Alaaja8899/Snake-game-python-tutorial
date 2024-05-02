import pygame , random , sys , time 
from pygame.locals import *


pygame.init()

dis=pygame.display.set_mode([720,480])
pygame.display.set_caption('snake')

snake_pos = [100,50]
snake_body = [[100,50],[100-10,50],[100-(2*10),50]]

food_pos = [random.randint(0,720//10)*10,random.randint(0,480//10)*10]


right = True 
left = False
up = False
down = False
timer = pygame.time.Clock()
while True:
	timer.tick(30)
	dis.fill('black')
	food = pygame.draw.rect(dis , 'yellow' , [food_pos[0],food_pos[1] , 10,10])
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	for pos in snake_body:
		pygame.draw.rect(dis , 'green', [pos[0],pos[1],10,10])


	key_pressed  = pygame.key.get_pressed()
	snake_body.insert(0,list(snake_pos))
	if key_pressed[K_RIGHT]:
		right = True 
		left = False
		up = False
		down = False
	elif key_pressed[K_LEFT]:
		right = False 
		left = True
		up = False
		down = False
	elif key_pressed[K_UP]:
		right = False 
		left = False
		up = True
		down = False
	elif key_pressed[K_DOWN]:
		right = False 
		left = False
		up = False
		down = True

	if right:
		snake_pos[0]+=10
	elif left:
		snake_pos[0]-=10
	elif up:
		snake_pos[1]-=10
	elif down:
		snake_pos[1]+=10

	if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
		print('collide')
		food_pos = [random.randint(0,720//10)*10,random.randint(0,480//10)*10]

	else:
		snake_body.pop()
	pygame.display.update()


pygame.quit()