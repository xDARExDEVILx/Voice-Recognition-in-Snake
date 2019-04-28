import pygame
import random
import time
import copy

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
MID = (200, 200, 200)
YELLOW = (255, 255,  0)
FRUITY = ( 22, 250, 73)
HEADDY = ( 233, 156, 0)

screen_width = 600
screen_height = 600

class Board:
    
    arr = []
    obst = [[2,2],[7,7],[2,7],[7,2]]
    fruit_pos = []
    score = 0
    
    def __init__(self):
        
        for x in range(0,10):
            self.arr.append([0,0,0,0,0,0,0,0,0,0])
        
    def display(self, surface):
        
        for y in range(0,10):
            for x in range(0,10):
                pygame.draw.rect(surface, MID, (50 + x * 50, 50 + y * 50, 45, 45))
            
        for obst in self.obst:
            pygame.draw.rect(surface, BLACK, (50 + 50 * obst[0], 50 + 50 * obst[1], 45, 45))
                
        pygame.draw.rect(surface, FRUITY, (50 + 50 * self.fruit_pos[0], 50 + 50 * self.fruit_pos[1], 45, 45)) # fruit    
        
        pygame.display.set_caption("Snake - points: " + str(self.score)) # score in upper bar
    
    def place_fruit(self, sneak):
        
        forbidden_places = self.obst + sneak.parts
        
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            
            if [x,y] not in forbidden_places:
                self.fruit_pos = [x,y]
                break
                 
class Snake:
           
    def __init__(self):
        self.restart()
        self.counter_base = 45
       
    def restart(self):
        self.parts = [[4,8]]
        self.dir = 'up'
        self.speed = 1
        self.belly_full = False
        self.counter = 0
       
    def display(self, surface):
        for part in self.parts:
            pygame.draw.rect(surface, YELLOW, (50 + 50 * part[0], 50 + 50 * part[1], 45, 45))

        pygame.draw.rect(surface, HEADDY, (50 + 50 * self.parts[0][0], 50 + 50 * self.parts[0][1], 45,45 ))
        
    def move_up(self):
        
        if self.belly_full == True:
            self.parts.insert(0, [self.parts[0][0] , self.parts[0][1] - 1])
            self.belly_full = False
        else:
            self.parts.insert(0, [self.parts[0][0] , self.parts[0][1] - 1])
            self.parts.pop()
     
    def move_down(self):
        
        if self.belly_full == True:
            self.parts.insert(0, [self.parts[0][0] , self.parts[0][1] + 1])
            self.belly_full = False
        else:
            self.parts.insert(0, [self.parts[0][0] , self.parts[0][1] + 1])
            self.parts.pop()
            
    def move_left(self):
        
        if self.belly_full == True:
            self.parts.insert(0, [self.parts[0][0] - 1, self.parts[0][1]])
            self.belly_full = False
        else:
            self.parts.insert(0, [self.parts[0][0] - 1 , self.parts[0][1]])
            self.parts.pop()

    def move_right(self):
        
        if self.belly_full == True:
            self.parts.insert(0, [self.parts[0][0] + 1, self.parts[0][1]])
            self.belly_full = False
        else:
            self.parts.insert(0, [self.parts[0][0] + 1, self.parts[0][1]])
            self.parts.pop()
    
    def faster(self):
        if self.counter_base > 20:
            self.counter_base = self.counter_base - 10
    
    def slower(self):
        self.counter_base = self.counter_base + 10
    
    def move_activator(self):
        if self.counter == self.counter_base:
            self.counter = 0
                                   
            if self.dir == 'up':
                self.move_up()
            elif self.dir == 'down':
                self.move_down()
            elif self.dir == 'left':
                self.move_left()
            elif self.dir == 'right':
                self.move_right()
        else:
            self.counter += 1

    def input(self, key):
        
        if key == pygame.K_UP:
            if self.dir != 'up' and self.dir != 'down':
                self.dir = 'up'
        if key == pygame.K_DOWN:
            if self.dir != 'up' and self.dir != 'down':
                self.dir = 'down'
        if key == pygame.K_LEFT:
            if self.dir != 'left' and self.dir != 'right':
                self.dir = 'left'
        if key == pygame.K_RIGHT:
            if self.dir != 'left' and self.dir != 'right':
                self.dir = 'right'
        if key == pygame.K_m:
            self.faster()
        if key == pygame.K_n:
            self.slower()
        

        
class Judge:

    def restart(self, sneak, board):
        sneak.restart()
        board.place_fruit(sneak)
        board.score = 0
        time.sleep(1)
        
    def collision_obstacle(self, sneak, board):
        head = sneak.parts[0]
        obst = board.obst
        
        if head in obst or head[0] > 9 or head[0] < 0 or head[1] > 9 or head[1] < 0 :
            self.restart(sneak, board)
          
    def collision_fruit(self, sneak, board):
        head = sneak.parts[0]
        if head == board.fruit_pos:
            sneak.belly_full = True
            board.place_fruit(sneak)
            board.score += 1
    
    def collision_self(self, sneak, board):
        
        head = sneak.parts[0]
        tail = copy.copy(sneak.parts)
        tail.pop(0)
        
        if head in tail:
            self.restart(sneak, board)
            
            
b1 = Board()
s1 = Snake()
j1 = Judge()
    
b1.place_fruit(s1)    
    
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake - points: 0")

clock = pygame.time.Clock()

on = True

while on:
   
    screen.fill(BLACK)
    b1.display(screen)
    s1.display(screen)
    
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        elif event.type == pygame.KEYDOWN:
            s1.input(event.key)
        
    s1.move_activator()
    j1.collision_obstacle(s1, b1)
    j1.collision_fruit(s1,b1)
    j1.collision_self(s1,b1)
   
pygame.quit()
