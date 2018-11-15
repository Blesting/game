import math
from random import randint
import collections
from level import Level

class Game():
        def __init__(self):
                self.state = 0
                #State 0: Menu
                #State 1: Game
                #State 2: Pause
                self.x = 100
                self.y = 100
                self.points = 0
                self.target = [250, 250]
                self.moveCool = 0
                self.moveCoolSet = 20
                self.snake = collections.deque([])
                self.snake.appendleft((self.x,self.y))
                self.snakeLength = 4
                self.direction = 0
                self.hold = False
                self.level = Level()
                self.currentLevel = 1
                

        def tick(self, pg, pressed):
            if self.state == 1:
                if self.FindDuplicates(self.snake) == True:
                    self.state = 0
                    self.start_game()
                if pressed[pg.K_RIGHT] and self.direction !=2: 
                    self.direction = 0 
                if pressed[pg.K_DOWN] and self.direction !=3:
                    self.direction = 1
                if pressed[pg.K_LEFT] and self.direction !=0: 
                    self.direction = 2
                if pressed[pg.K_UP]  and self.direction !=1:
                    self.direction = 3
                if self.moveCool == 0:
                    if pressed:
                        if pressed[pg.K_RIGHT] and not self.hold and self.direction !=2: 
                            self.hold = True
                            self.direction = 0 
                        if pressed[pg.K_DOWN] and not self.hold and self.direction !=3: 
                            self.hold = True
                            self.direction = 1
                        if pressed[pg.K_LEFT] and not self.hold and self.direction !=0: 
                            self.hold = True
                            self.direction = 2
                        if pressed[pg.K_UP] and not self.hold and self.direction !=1: 
                            self.hold = True
                            self.direction = 3
                        if self.hold and not (pressed[pg.K_RIGHT] or pressed[pg.K_LEFT] or pressed[pg.K_DOWN] or pressed[pg.K_UP]):
                            self.hold = False
                        if pressed[pg.K_LSHIFT]:
                            self.moveCoolSet = 10
                        elif pressed[pg.K_SPACE]:
                            self.moveCoolSet = 100
                        else:
                            self.moveCoolSet = 20
                        
                    if self.direction == 0: #right
                        self.x += 50
                        self.moveCool = self.moveCoolSet
                        self.snake.appendleft((self.x,self.y))
                    elif self.direction == 1: #down
                        self.y += 50
                        self.moveCool = self.moveCoolSet
                        self.snake.appendleft((self.x,self.y))
                    elif self.direction == 2: #left
                        self.x -= 50
                        self.moveCool = self.moveCoolSet
                        self.snake.appendleft((self.x,self.y))
                    elif self.direction == 3: #up
                        self.y -= 50
                        self.moveCool = self.moveCoolSet
                        self.snake.appendleft((self.x,self.y))
                    
                    if math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2) < 40:
                            self.points += 1
                            self.snakeLength += 1
                            self.target = [(50*randint(0,15)), (50*randint(0,11))]
                if self.moveCool > 0:
                    self.moveCool -= 1
                if self.moveCool < 0:
                    self.moveCool = 0
                if len(self.snake) > self.snakeLength:
                    self.snake.pop()

                if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
                    self.state = 0
                    self.start_game()
            
        def FindDuplicates(evt,liste):  
            unique = set(liste) 
            for each in unique:  
                count = liste.count(each)  
                if count > 1:
                    return True
            return False
        
        def start_game(self):
                if self.state == 0:
                        self.state = 1     
                        self.points = 0
                        self.x = 100
                        self.y = 100
                        self.target = [(50*randint(0,15)), (50*randint(0,11))]
                        self.direction = 0
                        self.snake.clear()
                        self.snakeLength = 4
                        self.x = 100
                        self.y = 100
                        self.level.create_level()
                        #self.level.create_level(self.currentLevel)

        def end_game(self):
                if self.state > 0:
                        self.state = 0

        def toggle_pause(self):
                if self.state == 1:
                        self.state = 2
                else:
                        self.state = 1

        def started(self):
                if self.state > 0:
                        return True
                else:
                        return False
        def create_Room(self, obsList):
            for i in self.room.obsList:
                #pygame.draw.rect(screen, (123,50,10), pygame.Rect(i[0], i[1], 50, 50))
                pass
                
                
                
                
                
                
                
                
                
                
