from random import randint
from enemies import Enemy

class Room():
    def __init__(self):
        self.naboCount = randint(1,4)
        self.roomId = 0
        self.enemy = None
        self.obsList = []
    
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
            
        
    def endRoom_create(self):
        pass
    
    def make_room(self,enemyCount,obsCount):
        self.obsList = []
        print(2)
        for i in range(3):
            self.obsList.append((50*randint(1,14), 50*randint(1,10)))
        print(self.obsList)
        '''enemyList = []
        for i in range(enemyCount):
            Enemy(50*randint(1,14), 50*randint(1,10), randint(0,1))
        self.enemy = Enemy(50*randint(1,14), 50*randint(1,10), randint(0,1))
        '''
        #self.game.create_room(obsList, enemyList)