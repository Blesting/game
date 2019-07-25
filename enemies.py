from random import randint
from projectile import Projectile

class Enemy:
    def __init__(self, x, y, type):
        self.eX = x
        self.eY = y
        self.eType = type
        self.eState = True
        self.eDirection = randint(0,3)
        self.eCool = 0
        self.projectileList = []
        
        
    def enemy_move(self):
        if self.eType == 1:
            if self.eCool < 0:
                if self.eDirection == 0 or self.eDirection == 1:
                    p = Projectile(self.eX, self.eY, 0)
                    self.projectileList.append(p)
                    p = Projectile(self.eX, self.eY, 1)
                    self.projectileList.append(p)
                    
                    self.eDirection = 2
                elif self.eDirection == 2 or self:
                    p = Projectile(self.eX, self.eY, 2)
                    self.projectileList.append(p)
                    p = Projectile(self.eX, self.eY, 3)
                    self.projectileList.append(p)
                    self.eDirection = 0
                self.eCool = 200
                
            else:
                self.eCool -= 1
            
            
            
        elif self.eType == 0:
            if self.eCool < 0:
                if self.eDirection == 0 and self.eX > 650:
                    self.eDirection = 1
                elif self.eDirection == 1 and self.eX < 100:
                    self.eDirection = 0
                elif self.eDirection == 2 and self.eY > 450:
                    self.eDirection = 3
                elif self.eDirection == 3 and self.eY < 100:
                    self.eDirection = 2
                
                if self.eDirection == 0:
                    self.eX += 50
                elif self.eDirection == 1:
                    self.eX -= 50
                elif self.eDirection == 2:
                    self.eY += 50
                elif self.eDirection == 3:
                    self.eY -= 50
                    
                
                self.eCool = 40
            else:
                self.eCool -= 1
            #self.x < 50 or self.x > 700 or self.y < 50 or self.y > 500
            
        
        
        #return enemyList