# This is my version of the classic snake game
# This is the main recourse that I used
# https://realpython.com/pygame-a-primer/
# Import and initialize the pygame library
import pygame
import random
from pygame.locals import (
	K_w,
	K_a,
	K_s,
	K_d,
	K_UP,
	K_LEFT,
	K_DOWN,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT
)
# start game
pygame.init()


# TODO create shape and size of food sprite
class Food(pygame.sprite.Sprite):
	def __init__(self):
		super(Food, self).__init__()
		self.body = pygame.Surface((10, 10))
		self.body.fill((255, 255, 255))
		self.rect = self.body.get_rect()


# create snake claas
class Snake(pygame.sprite.Sprite):
	def __init__(self):
		super(Snake, self).__init__()
		self.body = pygame.Surface((10, 10))
		self.body.fill((255, 255, 255))
		self.rect = self.body.get_rect()

	# set up movements for snake
	def update(self, pressed_key):
		# TODO Right not you can't override up because the elifs, but without them it allows you to move diagonally
		# so fix movement
		if pressed_key[K_UP or K_w]:
			self.rect.move_ip(0, -5)
		elif pressed_key[K_LEFT or K_a]:
			self.rect.move_ip(-5, 0)
		elif pressed_key[K_RIGHT or K_d]:
			self.rect.move_ip(5, 0)
		elif pressed_key[K_DOWN or K_s]:
			self.rect.move_ip(0, 5)

		# Kill snake when it hits a wall
		if self.rect.left < 0:
			self.kill()
		if self.rect.right > SCREEN_WIDTH:
			self.kill()
		if self.rect.top < 0:
			self.kill()
		if self.rect.bottom > SCREEN_HEIGHT:
			self.kill()


game_speed = pygame.time.Clock()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# create groups for entiteis
food_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


# Create a custom event for adding a new enemy
ADDFOOD = pygame.USEREVENT + 1
ADDEVENT = pygame.event.Event(ADDFOOD)
#	pygame.time.set_timer(ADDFOOD, 2300)
# create instance of snake and add it to the group
python = Snake()
all_sprites.add(python)


# Run until the user asks to quit
running = True
while running:
	pygame.event.post(ADDEVENT)
	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		# Check for QUIT event. If QUIT, then set running to false.
		elif event.type == QUIT:
			running = False
		elif event.type == ADDFOOD:
			food = Food()
			food_group.add(food)
			all_sprites.add(food)

	ate_food = pygame.sprite.collide_rect(python, food)
	if ate_food:
		print('ate food')

	pressed_keys = pygame.key.get_pressed()

	python.update(pressed_keys)
	# if you don't fill after each move the snake works as a paint brush
	# This is how I will make the snake move
	# I will only have to paint over the tail of snake each time not the entire screen
	screen.fill((0, 0, 0))
	for thing in all_sprites:
		screen.blit(thing.body, thing.rect)
	pygame.display.flip()

	game_speed.tick(30)

# Done! Time to quit.
pygame.quit()
