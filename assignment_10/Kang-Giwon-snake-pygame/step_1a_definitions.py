import pygame, sys # sys: to use sys.exit()

pygame.init() # make paygame available for

screen = pygame.display.set_mode((750,750)) # blank canvas

pygame.display.set_caption("560 Snake Game") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

# When run, this returns Hello from the Pygame community. There is a canvas,
# bus we need the game loop for it to run.