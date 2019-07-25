from room import Room

class Level:
    def __init__(self):
        self.currentLevel = 1
        self.roomList = []
        self.levelSize = 0
        
        
    
    def create_level(self):
        self.roomList = []
        #self.room.make_room(self.currentLevel, self.currentLevel*2)
        #self.room.make_border()
        
        ID = 0
        x = 2 
        self.levelSize = (3 + self.currentLevel*2)
        while len(self.roomList) < self.levelSize:
            r = Room(ID, self.currentLevel*x, self.currentLevel)
            self.roomList.append(r)
            ID += 1
            x += 1
        for r in self.roomList:
            r.make_room()
            
        
        for i in range(0,len(self.roomList)):
            for r in self.roomList:
                if r.roomId == i:
                    for fr in self.roomList:
                        if fr.roomId == (i-1):
                            if fr.upDoor == 1:
                                r.downDoor = 1
                            if fr.rightDoor == 1:
                                r.leftDoor = 1
        
        for r in self.roomList:
            if r.roomId == self.levelSize-1:
                r.endDoor = True
            r.make_border()
            r.make_obs()
        
        