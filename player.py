import collections

class Player:
    def __init__(self, x, y, direction):
        self.x = 100
        self.y = 100
        self.moveCool = 0
        self.moveCoolSet = 20
        self.snakeLength = 4
        self.direction = 0
        self.hold = False
        self.snakeDirection = 0
        self.snake = collections.deque([])
        self.snake.appendleft((self.x,self.y, self.snakeDirection))
        
        
    def snake_move(self, pg, pressed):
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
        if self.moveCool < 0:
            if pressed:
                if pressed[pg.K_RIGHT] and not self.hold and self.direction !=2: 
                    self.hold = True
                    self.direction = 0 
                    self.snakeDirection = 0
                if pressed[pg.K_DOWN] and not self.hold and self.direction !=3: 
                    self.hold = True
                    self.direction = 1
                    self.snakeDirection = 1
                if pressed[pg.K_LEFT] and not self.hold and self.direction !=0: 
                    self.hold = True
                    self.direction = 2
                    self.snakeDirection = 2
                if pressed[pg.K_UP] and not self.hold and self.direction !=1: 
                    self.hold = True
                    self.direction = 3
                    self.snakeDirection = 3
                if self.hold and not (pressed[pg.K_RIGHT] or pressed[pg.K_LEFT] or pressed[pg.K_DOWN] or pressed[pg.K_UP]):
                    self.hold = False
                
                if pressed[pg.K_LSHIFT]:
                    self.moveCoolSet = 5
                elif pressed[pg.K_SPACE]:
                    self.moveCoolSet = 100
                else:
                    self.moveCoolSet = 20
            else:
                if self.direction == 0 or self.direction == 2:
                    self.snakeDirection = 4 
                elif self.direction == 1 or self.direction == 3:
                    self.snakeDirection = 5
            if self.direction == 0: #right
                self.x += 50
                self.moveCool = self.moveCoolSet
                self.snake.appendleft((self.x,self.y, self.snakeDirection))
            elif self.direction == 1: #down
                self.y += 50
                self.moveCool = self.moveCoolSet
                self.snake.appendleft((self.x,self.y, self.snakeDirection))
            elif self.direction == 2: #left
                self.x -= 50
                self.moveCool = self.moveCoolSet
                self.snake.appendleft((self.x,self.y, self.snakeDirection))
            elif self.direction == 3: #up
                self.y -= 50
                self.moveCool = self.moveCoolSet
                self.snake.appendleft((self.x,self.y, self.snakeDirection))
        else:
            self.moveCool -= 1
        if len(self.snake) > self.snakeLength:
            self.snake.pop()
    