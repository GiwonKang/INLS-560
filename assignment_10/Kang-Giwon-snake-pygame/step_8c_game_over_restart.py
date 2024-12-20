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
    def __init__(self, snake_body):
        #self.position = Vector2(5,6)
        self.position = self.generate_random_pos(snake_body)

    def draw(self):
            # food_rect = pygame.Rect(x, y, w, h) 
            food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
            # pygame.draw.rect(surface, color, rect)
            # pygame.draw.rect(screen, DARK_GREEN, food_rect)
            screen.blit(food_surface, food_rect)
            # return Vector2(x,y)
    
    def generate_random_cell(self):
          x = random.randint(0, number_of_cells -1)
          y = random.randint(0, number_of_cells -1)
          return Vector2(x,y)

    def generate_random_pos(self, snake_body):
         
         position = self.generate_random_cell()
         while position in snake_body:
              position = self.generate_random_cell()
         return position
    
class Snake:
    def __init__(self):
          self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)] # list in bracket
          self.direction = Vector2(1,0)
          self.add_segment = False 
    
    def draw(self):
         for segment in self.body:
              segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
              # pygame.draw.rect(screen, DARK_GREEN, segment_rect) switch comments
              pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7) # adjusted to round rectangle
    
    def update(self):
         self.body.insert(0, self.body[0] + self.direction)
         if self.add_segment == True:
              self.add_segment = False
         else:
              self.body = self.body[:-1] # : slicing that cells

    def reset(self):
         self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
         self.direction = Vector2(1, 0)

class Game:
    def __init__(self):
         self.snake = Snake()
         self.food = Food(self.snake.body)
         self.state = "RUNNING"
    
    def draw(self):
         self.food.draw()
         self.snake.draw()
    
    def update(self):
         if self.state == "RUNNING":
               self.snake.update()
               self.check_collision_with_food()    # added for eating
               self.check_collision_with_edges()
    
    def check_collision_with_food(self):
          if self.snake.body[0] == self.food.position: # added for eating, self.snake.body[0] = head
               self.food.position = self.food.generate_random_pos(self.snake.body) # deleted test pinrt("Eating food")
               self.snake.add_segment = True
               # print("Eating food")                    # added for testing
     
    def check_collision_with_edges(self):
         if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
              self.game_over()
         if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
              self.game_over()
     
    def game_over(self):
         self.snake.reset()
         self.food.position = self.food.generate_random_pos(self.snake.body)
         print("STOPPED")

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) 

pygame.display.set_caption("Retro Snake") # this is retro snake in the video

clock = pygame.time.Clock() # controls the frame rate of the game

game = Game() # comment food = Food() and snake = Snake()
# food = Food() # call the added function
# snake = Snake()
food_surface = pygame.image.load("graphics/food.png")

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
            if game.state == "STOPPED":
                 game.state = "RUNNING"
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

    # Now when game over, the game can be restarted by pressing any of the arrow keys.
    # The game is not over when the snake hits til. 