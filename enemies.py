

class Enemy:
    def __init__(self, x, y, type):
        self.eX = x
        self.eY = y
        self.eType = type
        self.eState = True
        
        self.make_enemy()
        
    def make_enemy(self, enemyList):
        enemyList.append(self.eX, self.eY, self.eType, self.eState)
        
        
        return enemyList