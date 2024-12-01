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

class Game:
    def __init__(self):
         self.snake = Snake()
         self.food = Food()
    
    def draw(self):
         self.food.draw()
         self.snake.draw()
    
    def update(self):
         self.snake.update()
         self.check_collision_with_food()    # added for eating
    
    def check_collision_with_food(self):
          if self.snake.body[0] == self.food.position: # added for eating, self.snake.body[0] = head
               self.food.position = self.food.generate_random_pos() # deleted test pinrt("Eating food")
               # print("Eating food")                    # added for testing

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("Retro Snake") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

game = Game() # comment food = Food() and snake = Snake()
# food = Food() # call the added function
# snake = Snake()

food_surface = pygame.image.load("Kang-Giwon-snake-pygame/graphics/food.png")

SNAKE_UPDATE = pygame.USEREVENT # Added to make snake go slower
pygame.time.set_timer(SNAKE_UPDATE, 200) # Snake moving very fast

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update() # Replaced snake.update() with game.update()
            # snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):    # added game
                  game.snake.direction = Vector2(0, -1)   # added game.
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                 game.snake.direction = Vector2(0, 1)     # added game.
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                 game.snake.direction = Vector2(-1, 0)    # added game.
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                 game.snake.direction = Vector2(1, 0)
    
    # Drawing
    screen.fill(GREEN)
    game.draw() # Deleted food.draw() and snake.draw()
    # food.draw() # now you can run and see the food rectangle
    # snake.draw() # View screen and see the snake and the food
    pygame.display.update()
    clock.tick(60)

    # nothing really looks different, but we are making sure that a random
    # food is not created on the snake. Do a compare dif to see the code changes.