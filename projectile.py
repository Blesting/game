
class Projectile:
    def __init__(self, pX, pY, pDirection):
        self.pX = pX
        self.pY = pY
        self.pDirection = pDirection
        self.pMoveCool = 0
        self.pState = True
        
    def projectile_move(self):
        if self.pMoveCool < 0:
            if self.pDirection == 0:
                self.pX += 50
            elif self.pDirection == 1:
                self.pX -= 50
            elif self.pDirection == 2:
                self.pY += 50
            elif self.pDirection == 3:
                self.pY -= 50
                
            self.pMoveCool = 50
        else:
            self.pMoveCool -= 1
        
        if self.pX < 50 or self.pX > 700 or self.pY < 50 or self.pY > 500:
            self.pState = False
                    #self.x < 50 or self.x > 700 or self.y < 50 or self.y > 500
                