import pygame, sys # sys: to use sys.exit()

pygame.init() # make paygame available for

screen = pygame.display.set_mode((750,750)) # blank canvas

pygame.display.set_caption("560 Snake Game") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)

    # When run, this presents a black screen.