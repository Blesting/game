from random import randint
from enemies import Enemy

class Room():
    def __init__(self, roomID, obsCount, enemyCount):
        self.naboCount = randint(1,4)
        self.obsList = []
        self.border = []
        self.borderDoor = []
        self.borderEndDoor = []
        self.enemyList = []
        self.rState = 0
        self.upDoor = 0
        self.rightDoor = 0
        self.downDoor = 0
        self.leftDoor = 0
        self.obsCount = obsCount
        self.enemyCount = enemyCount
        self.roomId = roomID
        self.endDoor = False
    
    def startRoom_create(self):
        pass
        
    
    def nabo_create(self):
        for i in range (self.naboCount):
            self.roomId += 1
            naboPos = randint(0,3)
            if naboPos == 0:
                self.level.append(self.roomId,naboPos)
            elif naboPos == 1:
                self.level.append(self.roomId,naboPos)
            elif naboPos == 2:
                self.level.append(self.roomId,naboPos)
            elif naboPos == 3:
                self.level.append(self.roomId,naboPos)
            
        
    
    def make_border(self):
        self.borderDoor = []
        self.border = []
        self.borderEndDoor = []
        if self.rState == 0:
            for i in range(0,16):
                self.border.append((50*i, 0))
                self.border.append((50*i, 50*11))
            for i in range(1,11):
                self.border.append((0, 50*i))
                self.border.append((15*50, 50*i))
            
            if self.rightDoor == 1:
                for i in range(4,8): 
                    self.borderDoor.append((15*50, 50*i))
            if self.leftDoor == 1:
                for i in range(4,8):
                    self.borderDoor.append((0, 50*i))
            if self.upDoor == 1:
                for i in range(6,10): 
                    self.borderDoor.append((50*i, 0))
            if self.downDoor == 1:
                for i in range(6,10): 
                    self.borderDoor.append((50*i, 11*50))
            #self.game.create_room(obsList, enemyList)
        elif self.rState == 1: # ikke længere i brug
            for i in range(0,16):
                self.border.append((50*i, 0))
                self.border.append((50*i, 50*11))
            for i in range(1,11):
                self.border.append((0, 50*i))
                if i != 4 and i != 5 and i != 6 and i != 7:
                    self.border.append((15*50, 50*i))
        elif self.rState == 2:
            for i in range(0,11):
                if i != 4 and i != 5 and i != 6 and i != 7:
                    self.border.append((15*50, 50*i))
                    self.border.append((0, 50*i))
            for i in range(0,16):
                if i != 6 and i != 7 and i != 8 and i != 9:
                    self.border.append((50*i, 11*50))
                    self.border.append((50*i, 0))
            if self.rightDoor == 0:
                for i in range(4,8): 
                    self.border.append((15*50, 50*i))
            if self.leftDoor == 0:
                for i in range(4,8):
                    self.border.append((0, 50*i))
            if self.upDoor == 0:
                for i in range(6,10): 
                    self.border.append((50*i, 0))
            if self.downDoor == 0:
                for i in range(6,10): 
                    self.border.append((50*i, 11*50))
            if self.endDoor == True:
                if self.rightDoor == 1:
                    for i in range(4,8): 
                        self.borderEndDoor.append((15*50, 50*i))
                if self.upDoor == 1:
                    for i in range(6,10): 
                        self.borderEndDoor.append((50*i, 0))
    
    def make_room(self):
        self.rState = 0
        self.upDoor = randint(0,1)
        self.rightDoor = randint(0,1)
        
        #while self.downDoor == 0 and self.leftDoor == 0:
         #   self.downDoor = randint(0,1)
          #  self.leftDoor = randint(0,1)
        
        while (self.upDoor == 0 and self.rightDoor == 0) or (self.upDoor == 1 and self.rightDoor == 1):
            self.upDoor = randint(0,1)
            self.rightDoor = randint(0,1)
            
        #print(self.upDoor, self.rightDoor, self.downDoor, self.leftDoor)
    def make_obs(self):
        self.obsList = []
        for i in range(self.obsCount):
            o = (50*randint(1,14), 50*randint(1,10))
            if self.rightDoor == 1:
                if self.leftDoor == 1:
                    while (o[0] < 50*5 or o[0] > 500) and o[1] > 3*50 and o[1] < 8*50:
                        o = (50*randint(1,14), 50*randint(1,10))
                if self.downDoor == 1:    
                    while (o[0] > 500 and o[1] > 3*50 and o[1] < 8*50) or (o[0] > 5*50 and o[0] < 10*50 and o[1] > 350):
                        o = (50*randint(1,14), 50*randint(1,10))
                else:
                    while (o[0] < 50*5 or o[0] > 500) and o[1] > 3*50 and o[1] < 8*50:
                        o = (50*randint(1,14), 50*randint(1,10))
            if self.upDoor == 1:
                if self.leftDoor == 1:
                    while (o[0] < 50*5 and o[1] > 3*50 and o[1] < 8*50) or (o[0] > 5*50 and o[0] < 10*50 and o[1] < 5*50):
                        o = (50*randint(1,14), 50*randint(1,10))
                if self.downDoor == 1:
                    while o[0] > 5*50 and o[0] < 10*50 and (o[1] > 350 or o[1] < 5*50):
                        o = (50*randint(1,14), 50*randint(1,10))
                else:
                    while (o[0] < 50*5 and o[1] > 3*50 and o[1] < 8*50) or (o[0] > 5*50 and o[0] < 10*50 and o[1] < 5*50):
                        o = (50*randint(1,14), 50*randint(1,10))
            self.obsList.append(o)
            
            
        self.enemyList = []
        for i in range(self.enemyCount):
            e = Enemy(50*randint(1,14), 50*randint(1,10), randint(0,1))
            for o in self.obsList:
                while (o[0] == e.eX and o[1] == e.eY) or (e.eX < 50*5 and e.eY > 4*50 and e.eY < 8*50):
                    e = Enemy(50*randint(1,14), 50*randint(1,10), randint(0,1))
            self.enemyList.append(e)
        
        
        