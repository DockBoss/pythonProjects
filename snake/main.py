# This is my version of the classic snake game
# This is the main recourse that I used
# https://realpython.com/pygame-a-primer/
# Import and initialize the pygame library
import pygame

from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_UP,
    K_LEFT,
    K_DOWN,
    K_RIGHT,
    KEYDOWN,
    QUIT
)

pygame.init()

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((20, 20))
# Give the surface a color to separate it from the background
surf.fill((255, 255, 255))
# find center of snake
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)


# Run until the user asks to quit
running = True
while running:
    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, surf_center)
    pygame.display.flip()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                pass
            elif event.key == K_a or event.key == K_LEFT:
                pass
            elif event.key == K_s or event.key == K_DOWN:
                pass
            elif event.key == K_d or event.key == K_RIGHT:
                pass

        elif event.type == QUIT:
            running = False



# Done! Time to quit.
pygame.quit()
