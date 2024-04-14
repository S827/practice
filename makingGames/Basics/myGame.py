import pygame, sys #import pygame module and sys modules
from pygame.locals import *  # imports locals from pygame module

# function call after importing pygame module and before calling any other
# pygame functions.
pygame.init()

# calling display function from pygame and set_mode function of display
# to create a window of size 1000, 800 which is taken as tuple argument
# and a pygame.Surface object will be returned, which is stored in DISPLAYSURF variable
DISPLAYSURF = pygame.display.set_mode((1000, 800))

# calling display.set_caption function and passing a string to make it
# the game title
pygame.display.set_caption("*****************My GAME******************")

while True:   # main game loop which will handle events
    # the list of event objects returned from pygame.event.get() will be
    # in order that the events happened and it will be iterated in for loop 
    for event in pygame.event.get():
        if event.type == QUIT: # checks if event type is QUIT Or not
            pygame.quit() #opposite of pygame.init(), deactivates pygame lib
            sys.exit()
    pygame.display.update() #surface object stored in DISPLAYSIRF will be redrawn
    
