import pygame
from game import Game


def draw_game():
                if game.state == 0:
                        pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
                        screen.blit(myfont.render("MENU", 1, (255,255,255)), (400, 300))
                elif game.state == 1:
                        screen.fill((0,10,20))
                        for r in game.level.roomList:
                            if r.roomId == game.currentRoom:
                                for i in r.obsList:
                                    pygame.draw.rect(screen, (50,50,50), pygame.Rect(i[0], i[1], 50, 50))
                                for i in r.border:
                                    pygame.draw.rect(screen, (30,30,30), pygame.Rect(i[0], i[1], 50, 50))
                                for i in r.borderDoor:
                                    pygame.draw.rect(screen, (70,70,70), pygame.Rect(i[0], i[1], 50, 50))
                                for i in r.borderEndDoor:
                                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(i[0], i[1], 50, 50))
                                for i in r.enemyList:
                                    pygame.draw.rect(screen, (250,50,50), pygame.Rect(i.eX, i.eY, 50, 50)) 
                                    for p in i.projectileList:
                                        pygame.draw.rect(screen, (250,250,50), pygame.Rect(p.pX, p.pY, 50, 50))
                        pygame.draw.rect(screen, (123,50,10), pygame.Rect(game.target[0], game.target[1], 50, 50))
                        '''for i in range(len(game.snake)):
                            if i != 0 and i != len(game.snake):
                                nu = game.snake[i]
                                efter = game.snake[i+1]
                                if nu[2] == før[2]:
                                    if nu[2] == 0 or nu[2] == 2:
                                        sprite = game.sprites[0]
                                    
                                    screen.blit(sprite,(nu[0],nu[1]))
                            
                            else:
                                nu = game.snake[i]
                                pygame.draw.rect(screen, (10,123,50), pygame.Rect(nu[0], nu[1], 50, 50))'''
                        for i in game.snake:
                            pygame.draw.rect(screen, (10,123,50), pygame.Rect(i[0], i[1], 50, 50))
                        
                        
                        screen.blit(myfont.render("Points: {}".format(game.points), 1, (255,255,0)), (60, 15))
                        screen.blit(myfont.render("Level: {}".format(game.level.currentLevel), 1, (255,255,0)), (180, 15))
                        screen.blit(myfont.render("Room: {}".format(game.currentRoom), 1, (255,255,0)), (300, 15))
                                
                            
                elif game.state == 2:
                        pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
                        screen.blit(myfont.render("PAUSE", 1, (255,255,255)), (400, 300))
                #print(pygame.key.get_pressed())

pygame.init()
screen = pygame.display.set_mode((800, 600))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        game.toggle_pause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        if game.started():
                                game.end_game()
                        else:
                                game.start_game()
        
        pressed = pygame.key.get_pressed()
        game.tick(pygame, pressed)
        draw_game()
        
        pygame.display.flip()
        clock.tick(60)

