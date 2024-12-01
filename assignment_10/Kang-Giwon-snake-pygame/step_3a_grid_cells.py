import pygame, sys # sys: to use sys.exit()

pygame.init() # make paygame available for
# CONSTANT with Capital Words, add Green and Dark Green
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
# Add cell size and number of cells GRID INTRO 12:57
cell_size = 30 # 30 pixels
number_of_cells = 25 # 25 x 25 grid

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("560 Snake Game") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # fill screen with GREEN
    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)

    # When run, this presents a lightgreen screen.