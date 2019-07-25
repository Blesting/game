import math
from random import randint
import collections
from level import Level
import pygame
import sqlite3

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
                self.snakeLength = 4
                self.direction = 0
                self.hold = False
                self.level = Level()
                '''
                try:
                        #.convert() converterer billedet til det format, der
                        #er valgt med pyamge.display.setmode(). Hurtigere tegning hver gang
                        self.sheet = pygame.image.load("SnakeSprite.PNG").convert_alpha()

                except pygame.error:
                        pass
                rects = ((6,6,56,56),(6,6,56,56),(6,6,56,56),(6,6,56,56),(6,6,56,56),(6,6,56,56))
                self.sprites = []
                
                for r in rects:
                        image = pygame.Surface(pygame.Rect(r).size, pygame.SRCALPHA, 32).convert_alpha()
                        image.blit(self.sheet, (0, 0), pygame.Rect(r))
                        self.sprites.append(image)'''
                
                self.currentLevel = 1
                self.currentRoom = 0
                self.entrance = 0
                self.snakeDirection = 0
                self.snake = collections.deque([])
                self.snake.appendleft((self.x,self.y, self.snakeDirection))
                
                #Scoreboard
                
                self.conn =sqlite3.connect("scoreboard.db")
                self.cursor = self.conn.cursor()
                self.conn.commit()
                try:
                    self.cursor.execute('''
                                        CREATE TABLE scoreboard(
                                       Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       Name TEXT,
                                       Score INTEGER
                                       );
                    ''')
                    self.conn.commit()

                except:
                    pass
                

                

        def tick(self, pg, pressed):
            if self.state == 1:
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
                    
                    if math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2) < 40:
                            self.points += 1
                            self.snakeLength += 1
                            self.target = [(-50), (-50)]
                            for r in self.level.roomList:
                                if r.roomId == self.currentRoom:
                                    r.rState = 2
                                    r.make_border()
                else:
                    self.moveCool -= 1
                if len(self.snake) > self.snakeLength:
                    self.snake.pop()
                        
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        for e in r.enemyList:

                            e.enemy_move()
                            
                            if e.eCool < 0:
                                for o in r.obsList:
                                    if e.eX == o[0] and e.eY == o[1]:
                                            if e.eDirection == 1:
                                                e.eDirection = 0
                                            elif e.eDirection == 0:
                                                e.eDirection = 1
                                            elif e.eDirection == 2:
                                                e.eDirection = 3
                                            elif e.eDirection == 3:
                                                e.eDirection = 2
                            
                            for p in e.projectileList:
                                p.projectile_move()
                                for o in r.obsList:
                                    if p.pX == o[0] and p.pY == o[1]:
                                        p.pState = False
                                if p.pState == False:
                                    e.projectileList.remove(p)
            
                
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        for e in r.enemyList:
                            if self.x == e.eX and self.y == e.eY:
                                e.eState = False
                            for s in list(self.snake):
                                if s[0] == e.eX and s[1] == e.eY and e.eState == True:
                                    self.state = 0
                                    self.start_game()

                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        for e in r.enemyList:
                            if e.eState == False:
                                r.enemyList.remove(e)

                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        if r.rState == 0:
                            if self.x < 50 or self.x > 700 or self.y < 50 or self.y > 500:
                                self.state = 0
                                self.start_game()
                        elif r.rState == 1 or r.rState == 2:
                            if self.x > 700 and (self.y < 4*50 or self.y > 7*50):
                                    self.state = 0
                                    self.start_game()
                            if self.x < 50 and (self.y < 4*50 or self.y > 7*50):
                                    self.state = 0
                                    self.start_game()
                            if self.y > 500 and (self.x < 6*50 or self.x > 9*50):
                                    self.state = 0
                                    self.start_game()
                            if self.y < 50 and (self.x < 6*50 or self.x > 9*50):
                                    self.state = 0
                                    self.start_game()
                
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        if self.x > 700 and not(self.y < 4*50 or self.y > 7*50):
                                if r.rightDoor == 1:
                                    self.entrance = 0
                                    self.game_forward()
                                else:
                                    self.state = 0
                                    self.start_game()
                        if self.x < 50 and not(self.y < 4*50 or self.y > 7*50):
                                if r.leftDoor == 1:
                                    self.entrance = 2
                                    self.game_backward()
                                else:
                                    self.state = 0
                                    self.start_game()
                        if self.y > 500 and not(self.x < 6*50 or self.x > 9*50):
                                if r.downDoor == 1:
                                    self.entrance = 1
                                    self.game_backward()
                                else:
                                    self.state = 0
                                    self.start_game()
                        if self.y < 50 and not(self.x < 6*50 or self.x > 9*50):
                                if r.upDoor == 1:
                                    self.entrance = 3
                                    self.game_forward()
                                else:
                                    self.state = 0
                                    self.start_game()
                
                projectileXY = []
                snakeXY = []
                for i in self.snake:
                    snakeXY.append((i[0],i[1]))
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        for e in r.enemyList:
                            for p in e.projectileList:
                                projectileXY.append((p.pX, p.pY))
                if (set(snakeXY) & set(projectileXY)):
                    self.state = 0
                    self.start_game()
                
                if self.FindDuplicates(snakeXY) == True:
                    self.state = 0
                    self.start_game()
                
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        if (set(snakeXY) & set(r.obsList)):
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
                        self.insert_highscore()
                        self.points = 0
                        self.x = 50
                        self.y = 50*6
                
                        self.direction = 0
                        self.snake.clear()
                        self.snakeLength = 4
                        self.level.currentLevel = 1
                        self.currentRoom = 0
                        self.level.create_level()
                        #self.level.create_level(self.currentLevel)
                        self.create_target()
                        
        def game_forward(self):
            if self.state == 1:
                if self.entrance == 0: # rightDoor
                    self.x = 50
                    self.direction = 0
                elif self.entrance == 3: # upDoor
                    self.y = 500
                    self.direction = 3
                
                self.snake.clear()
                self.snake.appendleft((self.x,self.y))

                #self.level.currentLevel += 1
                #self.level.create_level()
                
                if self.currentRoom == self.level.levelSize-1:
                    self.level.currentLevel += 1
                    self.currentRoom = 0
                    self.x = 50
                    self.y = 50*6
                    self.level.create_level()
                else:
                    self.currentRoom += 1
                
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        if r.rState == 0:
                            self.create_target()
        
        def game_backward(self):
            if self.state == 1:
                if self.entrance == 1: # downDoor
                    self.y = 50
                    self.direction = 1
                elif self.entrance == 2: # leftDoor
                    self.x = 700
                    self.direction = 2
        
                self.snake.clear()
                self.snake.appendleft((self.x,self.y))
                #self.level.currentLevel += 1
                #self.level.create_level() 
                self.currentRoom -= 1
                
                for r in self.level.roomList:
                    if r.roomId == self.currentRoom:
                        if r.rState == 0:
                            self.create_target()
                
        
        def insert_highscore(self):
            self.cursor.execute('''
                       INSERT INTO scoreboard
                       (Name, Score)
                       VALUES
                       ("Unknown", {});
                       '''.format(self.points))
            self.conn.commit()
            scoreboard = []
            place = 1
            for i in self.cursor.execute('''SELECT * FROM scoreboard 
                                         ORDER BY Score 
                                         DESC'''):
                scoreboard.append((place, i))
                place += 1
                
            for i in range(0,10):
                print(scoreboard[i])
                

        
        def create_target(self):
            self.target = [(50*randint(1,14)), (50*randint(1,10))]
            for s in self.snake:
                while s[0] == self.target[0] and s[1] == self.target[1]:
                    self.target = [(50*randint(1,14)), (50*randint(1,10))]
            for r in self.level.roomList:
                    for o in r.obsList:
                        while o[0] == self.target[0] and o[1] == self.target[1]:
                            self.target = [(50*randint(1,14)), (50*randint(1,10))]
        
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
                
                
                
                
                
                
                
                
                
                
