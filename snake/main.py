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
		#self.position = tuple(round(random.random() * 500, -1) for _ in range(2))

#created snake body
class Body(pygame.sprite.Sprite):
	def __init__(self):
		super(Body, self).__init__()
		self.body = pygame.surface

# create snake claas
class Snake(pygame.sprite.Sprite):
	def __init__(self):
		super(Snake, self).__init__()
		self.body = pygame.Surface((10, 10))
		self.body.fill((255, 255, 255))
		self.rect = self.body.get_rect()


	# set up movements for snake
	def update(self, direction):
		if direction == 1:
			self.rect.move_ip(0, -5)
		elif direction == 4:
			self.rect.move_ip(-5, 0)
		elif direction == 2:
			self.rect.move_ip(5, 0)
		elif direction == 3:
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
all_sprites = pygame.sprite.Group()


# Create a custom event for adding a new enemy
#TODO ADDFOOD = pygame.USEREVENT + 1
#TODO ADDEVENT = pygame.event.Event(ADDFOOD)

#create instance of snake and add it to the group
python = Snake()
all_sprites.add(python)

#create an instance of food and add it to the group
food = Food()
all_sprites.add(food)

direction = -1  # direction of snake -1 to start, so it won't move until a keypress

# Run until the user asks to quit
running = True
while running:
	#TODO pygame.event.post(ADDEVENT)
	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		# Check for QUIT event. If QUIT, then set running to false.
		elif event.type == QUIT:
			running = False
		"""elif event.type == ADDFOOD:
			food.kill()
			food = Food()
			print('didi it work')
			all_sprites.add(food)
	Will not work, snake is always colliding with itself
	if pygame.sprite.collide_rect(python, python):
		python.kill()
		running = False
	"""

	if pygame.sprite.collide_rect(python, food):
		print('ate food')
		# pygame.event.post(ADDFOOD)


	pressed_keys = pygame.key.get_pressed()
	#set direction baised on key presses
	if pressed_keys[K_UP] or pressed_keys[K_w]:
		if direction != 3:
			direction = 1
	elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
		if direction != 2:
			direction = 4
	elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
		if direction != 4:
			direction = 2
	elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
		if direction != 1:
			direction = 3
	python.update(direction)

	# if you don't fill after each move the snake works as a paint brush
	screen.fill((0, 0, 0))

	for thing in all_sprites:
		screen.blit(thing.body, thing.rect)

	# update screen
	pygame.display.flip()

	game_speed.tick(30)

# Done! Time to quit.
pygame.quit()