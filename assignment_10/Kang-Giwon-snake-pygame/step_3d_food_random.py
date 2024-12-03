import pygame, sys, random # sys: to use sys.exit(), define random
from pygame.math import Vector2 # for gird works

pygame.init() # make paygame available for
# CONSTANT with Capital Words, add Green and Dark Green
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
# Add cell size and number of cells GRID INTRO 12:57
cell_size = 30 # 30 pixels
number_of_cells = 25 # 25 x 25 grid

# create food class
class Food:
    def __init__(self):
        #self.position = Vector2(5,6) # hos to position the food specifically
        self.position = self.generate_random_pos() # makes food appear random

    def draw(self): # Display Surface | Surface | Rect
            # food_rect = pygame.Rect(x, y, w, h) 
            food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
            # pygame.draw.rect(surface, color, rect)
            # pygame.draw.rect(screen, DARK_GREEN, food_rect)
            screen.blit(food_surface, food_rect) # Now we have a food graphic!
    
    def generate_random_pos(self): # need to add random at top
         x = random.randint(0, number_of_cells -1)
         y = random.randint(0, number_of_cells -1)
         position = Vector2(x,y)
         return position

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("560 Snake Game") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

food = Food() # call the added function
food_surface = pygame.image.load("graphics/food.png") # Python image load

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # fill screen with GREEN
    screen.fill(GREEN)
    food.draw() # now you can run and see the food rectangle
    pygame.display.update()
    clock.tick(60)

    # Now when we run the program, it will place the food in a random position