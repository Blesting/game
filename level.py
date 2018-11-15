from random import randint
from room import Room

class Level:
    def __init__(self):
        self.currentLevel = 1
        self.level = []
        
        self.room = Room()
        
        
    
    def create_level(self):
        print(1)
        self.room.make_room(self.currentLevel, self.currentLevel*2)
        lvlSize = (self.currentLevel*5)
        for i in range (lvlSize):
            pass
        