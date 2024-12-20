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
        #self.position = Vector2(5,6)
        self.position = self.generate_random_pos()

    def draw(self):
            # food_rect = pygame.Rect(x, y, w, h) 
            food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
            # pygame.draw.rect(surface, color, rect)
            # pygame.draw.rect(screen, DARK_GREEN, food_rect)
            screen.blit(food_surface, food_rect)
    
    def generate_random_pos(self):
         x = random.randint(0, number_of_cells -1)
         y = random.randint(0, number_of_cells -1)
         position = Vector2(x,y)
         return position
    
class Snake:
    def __init__(self):
          self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)] # list in bracket
          self.direction = Vector2(1,0)
    
    def draw(self):
         for segment in self.body:
              segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
              # pygame.draw.rect(screen, DARK_GREEN, segment_rect) switch comments
              pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7) # adjusted to round rectangle
    
    def update(self):
         self.body = self.body[:-1] # : slicing that cells
         self.body.insert(0, self.body[0] + self.direction)

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("Retro Snake") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

food = Food() # call the added function
snake = Snake()
food_surface = pygame.image.load("graphics/food.png")

SNAKE_UPDATE = pygame.USEREVENT # Added to make snake go slower
pygame.time.set_timer(SNAKE_UPDATE, 200) # Snake moving very fast

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Vector2(0, 1):
                  snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                 snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                 snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                 snake.direction = Vector2(1, 0)
    
    # fill screen with GREEN
    screen.fill(GREEN)
    food.draw() # now you can run and see the food rectangle
    snake.draw() # View screen and see the snake and the food
    pygame.display.update()
    clock.tick(60)

    # Snake cannot reverse direction now.