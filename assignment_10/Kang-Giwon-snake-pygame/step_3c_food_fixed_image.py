import pygame, sys # sys: to use sys.exit()
from pygame.math import Vector2 # for gird works

pygame.init() # make paygame available for
# CONSTANT with Capital Words, add Green and Dark Green
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
# Add cell size and number of cells GRID INTRO 12:57
cell_size = 30 # 30 pixels
number_of_cells = 25 # 25 x 25 grid

class Food:
    def __init__(self):
        self.position = Vector2(5,6)

    def draw(self):
            # food_rect = pygame.Rect(x, y, w, h) # 19:00
            food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
            # pygame.draw.rect(surface, color, rect)
            # pygame.draw.rect(screen, DARK_GREEN, food_rect)
            screen.blit(food_surface, food_rect)

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("560 Snake Game") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

food = Food() # call the added function
food_surface = pygame.image.load("graphics/food.png")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # fill screen with GREEN
    screen.fill(GREEN)
    food.draw()
    pygame.display.update()
    clock.tick(60)

    # When run, this will show the food graphic. Proglem now is that it is
    # always going to be created at the same spot.