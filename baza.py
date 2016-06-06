import pygame
import random
import sys #to quit game when meteor kill you



"""SPACE - TURN ON / OFF SHIELD"""
"""X - change gun mode"""
  




"""colors"""
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (51,255,255)
orange = (255,215,0)
green = (51,255,51)
purple = (160,32,240)




"""Screen Size"""
screen_width = 800
screen_height = 600




""" pozition background"""
pozX = 0
pozY = 0



fps = 60
scare = 0 #frags /  number of destroy meteors



level = 0



nextLevel = 700 # points to change lvl


gameExit = False





class Player(pygame.sprite.Sprite):

    imageN = []
    imageN2 = []
    gun_index = 0
    live = 3
    
    
    def __init__(self):
        #wconstructor class up
        pygame.sprite.Sprite.__init__(self)

        self.imageN  = pygame.image.load("res/statek1.gif").convert() #ship when shield is off
        self.imageN2 = pygame.image.load("res/statek2.gif").convert() #ship when shield is on
        self.image = pygame.Surface([85,90])  
        self.image= self.imageN
        self.rect = self.image.get_rect() #return size
        self.shield = False
        self.shieldPoint = 100


    def update_gun(self):
        """gun mode 0 - one shoot , 1 - double shoot , 2 - triple shoot , 3 - five shoot"""
        self.gun_index +=1
        if self.gun_index == 4:
            self.gun_index = 0


    def upShieldPoint(self):
        if self.shieldPoint <= 100:
            self.shieldPoint +=1

            
    """aktivate and draw shield"""
    def run_shield(self):
        if self.shield == False:
            self.shield = True
            self.image= self.imageN2
            
        else:
            self.shield = False
            self.image= self.imageN

    def shield_down(self):
        self.shield = False
        self.image= self.imageN
            

    def get_shield(self):
        return self.shield







class Meteor(pygame.sprite.Sprite):
    imageN = []
    

    def __init__(self,index):

        #constructor class up
        pygame.sprite.Sprite.__init__(self)
        self.point = index

        if index == 5 :
            self.imageN  = pygame.image.load("res/0.gif").convert()
            self.image = pygame.Surface([101,84])
        if index == 6 :
            self.imageN  = pygame.image.load("res/1.gif").convert()
            self.image = pygame.Surface([120,98])
        if index == 3 :
            self.imageN  = pygame.image.load("res/2.gif").convert()
            self.image = pygame.Surface([43,43])
        if index == 4 :
            self.imageN  = pygame.image.load("res/3.gif").convert()
            self.image = pygame.Surface([45,40])
        if index == 1 :
            self.imageN  = pygame.image.load("res/4.gif").convert()
            self.image = pygame.Surface([28,28])
        if index == 2 :
            self.imageN  = pygame.image.load("res/5.gif").convert()
            self.image = pygame.Surface([29,26])
        if index == 0 :
            self.imageN  = pygame.image.load("res/6.gif").convert()
            self.image = pygame.Surface([18,18])

                    
       
        self.image= self.imageN
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.y +=1








class LiveDrop(pygame.sprite.Sprite):

    imageN = []
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imageN  = pygame.image.load("res/liveDrop.gif").convert()
        self.image = pygame.Surface([35,32])
        self.image= self.imageN
        self.rect = self.image.get_rect()



    def update(self):
        self.rect.y +=2

        


        
        

class Bullet(pygame.sprite.Sprite):
  
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if player.gun_index == 0:
            self.image = pygame.Surface([4,10])
            self.image.fill(orange)
            self.height = 10
            self.width = 4


        if player.gun_index == 1:
            self.image = pygame.Surface([4,15])
            self.image.fill(red)
            self.height = 15
            self.width = 4

        if player.gun_index == 2:
            self.image = pygame.Surface([4,20])
            self.image.fill(green)
            self.height = 20
            self.width = 4


        if player.gun_index == 3:
            self.image = pygame.Surface([6,25])
            self.image.fill(blue)
            self.height = 25
            self.width = 6

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -=5

        



            

class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([6,25])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y +=5






class Alien(pygame.sprite.Sprite):

    imageN = []
    healt = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imageN  = pygame.image.load("res/alien.gif").convert()
        self.image = pygame.Surface([190,110])
        self.image= self.imageN
        self.rect = self.image.get_rect()
        self. vector = 0
        self.width = 190
        self.height = 110
        self.healt = 100
        healt = self.healt
   

    """hit detection when player shoot to alien """
    def detectColision(self,x,y,w,h):
        if (self.rect.x + self.width >= x >=self.rect.x and self.rect.y + self.height >=y >= self.rect.y):
            self.healt -=1
            return True
        elif (self.rect.x + self.width >= x + w >= self.rect.x and self.rect.y + self.height >= y >=self.rect.y):
            self.healt -=1
            return True
        elif (self.rect.x + self.width >= x >=self.rect.x and  self.rect.y + self.height >= y + h >= self.rect.y):
            self.healt -=1
            return True
        elif (self.rect.x + self.width >= x + w >=self.rect.x and  self.rect.y + self.height >= y + h >= self.rect.y):
            self.healt -=1
            return True
        
    
            
    def update(self):
        if self.rect.y != 50:
            self.rect.y +=1
        if self.rect.x == player.rect.x or self.rect.x+ 80 == player.rect.x or self.rect.x +190 ==player.rect.x:
        
            enemy_bullet0 = BulletEnemy()
            enemy_bullet1 = BulletEnemy()
            enemy_bullet2 = BulletEnemy()
            enemy_bullet3 = BulletEnemy()
            enemy_bullet4 = BulletEnemy()
            enemy_bullet5 = BulletEnemy()
            
            enemy_bullet0.rect.x = self.rect.x + 15
            enemy_bullet0.rect.y = self.rect.y + 65
            enemy_bullet1.rect.x = self.rect.x + 65
            enemy_bullet1.rect.y = self.rect.y + 70
            enemy_bullet2.rect.x = self.rect.x + 80
            enemy_bullet2.rect.y = self.rect.y + 60
            enemy_bullet3.rect.x = self.rect.x + 105
            enemy_bullet3.rect.y = self.rect.y + 60
            enemy_bullet4.rect.x = self.rect.x + 120
            enemy_bullet4.rect.y = self.rect.y + 70
            enemy_bullet5.rect.x = self.rect.x + 175
            enemy_bullet5.rect.y = self.rect.y + 65
            
            all_sprites_list.add(enemy_bullet0)
            all_sprites_list.add(enemy_bullet1)
            all_sprites_list.add(enemy_bullet2)
            all_sprites_list.add(enemy_bullet3)
            all_sprites_list.add(enemy_bullet4)
            all_sprites_list.add(enemy_bullet5)
            
            allien_bullet_list.add(enemy_bullet0)
            allien_bullet_list.add(enemy_bullet1)
            allien_bullet_list.add(enemy_bullet2)
            allien_bullet_list.add(enemy_bullet3)
            allien_bullet_list.add(enemy_bullet4)
            allien_bullet_list.add(enemy_bullet5)
            

        """seting alien finaly position and movement"""
        if self.rect.y == 50:
            if self.vector == 0:
                if self.rect.x != 0:
                    self.rect.x -=1
                if self.rect.x == 0:
                    self.vector =1

            if self.vector == 1:
                if self.rect.x != 610:
                    self.rect.x +=1
                if self.rect.x == 610:
                    self.vector =0
                



"""inicjalization pygame"""
pygame.init()




"""FPS"""
fpsClock = pygame.time.Clock()
fpsClock.tick(fps)




"""Set displa mode"""
gameDisplay = pygame.display.set_mode((screen_width,screen_height))




"""game name"""
pygame.display.set_caption('Cosmic Shooter')




"""load images"""
tlo = pygame.image.load("res/kosmos.jpg").convert() #background lvl 0
tlo1 = pygame.image.load("res/kosmos1.jpg").convert() #background lvl 1
live = pygame.image.load("res/live.gif").convert()




"""list / tuples"""
all_sprites_list = pygame.sprite.Group() #list all sprites to draw
meteor_list = pygame.sprite.Group() #list all meteors do draw
bullet_list = pygame.sprite.Group() #bullets list
meteor_hit_list = pygame.sprite.Group() #list meteors to destroy
allien_bullet_list = pygame.sprite.Group() #list alien bullets
allien_hit_list = pygame.sprite.Group() #alien hits list
live_drop_list = pygame.sprite.Group() #list live






"""create 30 meteors in random positions"""
if level == 0:
    for i in range(30):
        x = random.choice(range(7))
        meteor = Meteor(x)
        meteor.rect.x = random.randrange(screen_width)-100
        z = random.choice(range(600))
        meteor.rect.y = -z #random.randrange(screen_h)
        meteor_list.add(meteor)
        all_sprites_list.add(meteor)
    



"""PLAYER"""
player = Player()


"""Alien"""
alien = Alien()

alien.rect.x = 300
alien.rect.y = -200


"""adding player to sprite list"""
all_sprites_list.add(player)




"""game loop"""
while gameExit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


        #"""EVENTS"""
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            """one shoot"""
            if player.gun_index == 0:
                bullet = Bullet()
                bullet.rect.x = player.rect.x + 34 #position bullet X
                bullet.rect.y = player.rect.y #position bullet Y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

                
            """double shoot"""
            if player.gun_index == 1:
                bullet = Bullet()
                bullet1 = Bullet()
                bullet.rect.x = player.rect.x +4 #position bullet X
                bullet.rect.y = player.rect.y + 25 #position bullet Y
                bullet1.rect.x = player.rect.x + 68  #position bullet1 X
                bullet1.rect.y = player.rect.y + 25#position bullet1 Y
                all_sprites_list.add(bullet)
                all_sprites_list.add(bullet1)
                bullet_list.add(bullet)
                bullet_list.add(bullet1)

                
            """triple shoot"""
            if player.gun_index == 2:
                bullet = Bullet()
                bullet1 = Bullet()
                bullet2 = Bullet()
                bullet.rect.x = player.rect.x +4 #position bullet X
                bullet.rect.y = player.rect.y + 25 #position bullet Y
                bullet1.rect.x = player.rect.x + 68  #position bullet1 X
                bullet1.rect.y = player.rect.y + 25#position bullet1 Y
                bullet2.rect.x = player.rect.x + 34 #position bullet X
                bullet2.rect.y = player.rect.y #position bullet Y
                all_sprites_list.add(bullet)
                all_sprites_list.add(bullet1)
                all_sprites_list.add(bullet2)
                bullet_list.add(bullet)
                bullet_list.add(bullet1)
                bullet_list.add(bullet2)



            """five shoots"""
            if player.gun_index == 3:
                bullet = Bullet()
                bullet1 = Bullet()
                bullet2 = Bullet()
                bullet3 = Bullet()
                bullet4 = Bullet()
                bullet.rect.x = player.rect.x +4     #position bullet X
                bullet.rect.y = player.rect.y + 25   #position bullet Y
                bullet1.rect.x = player.rect.x + 68  #position bullet1 X
                bullet1.rect.y = player.rect.y + 25  #position bullet1 Y
                bullet2.rect.x = player.rect.x + 34  #position bullet2 X
                bullet2.rect.y = player.rect.y       #position bullet2 Y
                bullet3.rect.x = player.rect.x + 14  #position bullet3 X
                bullet3.rect.y = player.rect.y + 10  #position bullet3 Y
                bullet4.rect.x = player.rect.x + 58  #position bullet4 X
                bullet4.rect.y = player.rect.y + 10  #position bullet4 Y
                all_sprites_list.add(bullet)
                all_sprites_list.add(bullet1)
                all_sprites_list.add(bullet2)
                all_sprites_list.add(bullet3)
                all_sprites_list.add(bullet4)
                bullet_list.add(bullet)
                bullet_list.add(bullet1)
                bullet_list.add(bullet2)
                bullet_list.add(bullet3)
                bullet_list.add(bullet4)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                player.update_gun()

            if event.key == pygame.K_SPACE:
                player.run_shield()







            
#"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!GAME FUNCTIONS!!!!!!!!!!!!!!!!!!"""


    
    #"""changing lvl """
    if scare >=nextLevel:
        if level == 0 :
            level+=1
            alien.index = 1
            #player.shieldPoint = 100
            font= pygame.font.Font(None, 120)
            text = font.render("Level 1",1,(255,255,255))
            pygame.Surface.convert_alpha(text)
            gameDisplay.blit(text,(400,300))
            pygame.display.flip()
            pygame.time.wait(500)
            





    
    """drawing background"""    
    if level == 0:
        gameDisplay.blit(tlo,(pozX,pozY))
    else:
        gameDisplay.blit(tlo1,(pozX,pozY))
        
        

        

    

    x =600 #only to help with position lives
    """player lives drawing"""
    if player.live > 0 and player.live<=3:
        for i in range (player.live):
            gameDisplay.blit(live,(x,550))
            x+=50
            if x >750:
                x= 600






    """mouse position and hero position"""
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0] - 42
    player.rect.y = pos[1] - 45




    


    """  BULLET - update bullet position , BULLET COLISION DETECT"""
    for bullet in bullet_list:
        bullet.update()
        #adding number to hit list meteors who is destroyd
        meteor_hit_list = pygame.sprite.spritecollide(bullet,meteor_list,True)

        if level > 0: #"""ALIEN BULLET DETECTION"""
            if alien.detectColision(bullet.rect.x, bullet.rect.y, bullet.width, bullet.height) == True:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                player.upShieldPoint()
                
    
       
      
        
        """removing bullet from lists"""
        for meteor in meteor_hit_list:
            scare += meteor.point
            player.upShieldPoint()
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
           
            
            
           
        """If bullet get out for screen"""
        if bullet.rect.y <-10:
               bullet_list.remove(bullet)
               all_sprites_list.remove(bullet)






    """ Allien Bullet """
    for enemy_bullet in allien_bullet_list:
        enemy_bullet.update()
        if player.get_shield() == False:
            allien_hit_list = pygame.sprite.spritecollide(player,allien_bullet_list,True)
            if len(allien_hit_list) == 1:    #IF detect colision player have -1 live , POSITION meteors is CHANGED!
                player.live -=1
        if player.get_shield() == True:
            allien_hit_list = pygame.sprite.spritecollide(player,allien_bullet_list,True)
            if len(allien_hit_list) == 1:    #IF detect colision player have -1 live , POSITION meteors is CHANGED!
                player.shieldPoint -=1
        


        """If bullet get out for screen"""
        if enemy_bullet.rect.y >600:
            allien_bullet_list.remove(enemy_bullet)
            all_sprites_list.remove(enemy_bullet)







    """adding meteor when was destruct and droping lives"""
    if level == 0:
        while len(meteor_list)<=40:
            x = random.choice(range(7))
            meteor = Meteor(x)
            
            if x == 0 or x ==1:
                """adding live to list live"""
                y = random.randrange(0,8)
                if y == 0:
                    heartDrop = LiveDrop()
                    heartDrop.rect.x = random.randrange(screen_width)-100
                    heartDrop.rect.y = -100
                    live_drop_list.add(heartDrop)
                    all_sprites_list.add(heartDrop)


            meteor.rect.x = random.randrange(screen_width)-100
            z = random.choice(range(400))
            meteor.rect.y = -z #random.randrange(screen_h)
            meteor_list.add(meteor)
            all_sprites_list.add(meteor)








    """update position live and remove when position > 600"""
    for heartDrop in live_drop_list:
        heartDrop.update()
        if heartDrop.rect.y >600:
            all_sprites_list.remove(heartDrop)
            live_drop_list.remove(heartDrop)
            


        


    heartDrop_hit_list = pygame.sprite.spritecollide(player,live_drop_list,True)
    if len(heartDrop_hit_list) == 1:
        if player.live <3:
            player.live+=1
        




        

    """gameplay for level 1 / ADDING ALIEN TO GAME , DRAW HIS LICE , DRAWING WINNER"""
    
    if level == 1:
        if alien.index == 1:
            all_sprites_list.add(alien) #adding alien to game
        alien.update()
        if alien.healt > 0:
            pygame.draw.rect(gameDisplay,red,(30,10,alien.healt*2,30))
        else:
            all_sprites_list.empty()
            font = pygame.font.Font(None, 120) #when player died , size text
            text = font.render("YOU WIN!!",1,(255,255,255))
            pygame.Surface.convert_alpha(text)
            gameDisplay.fill(black)
            gameDisplay.blit(text,(200,300)) #writen end game on display
            gameExit = True 
            
            
        
        
        



    """update meteor position // when lvl = 1 remove all meteors"""
    for meteor in meteor_list:
        meteor.update()
        if level ==0:
            if meteor.rect.y >600:
                meteor.rect.x = random.randrange(screen_width)-100
                z = random.choice(range(200))
                meteor.rect.y = -z #random.randrange(screen_h)
        else:
            if meteor.rect.y >600:
                meteor_list.remove(meteor)





                        
#"""kolizion detect with player when shield is on // False - penetration meteors"""
                            
    if player.get_shield() == True:
        meteor_hit_list = pygame.sprite.spritecollide(player,meteor_list,True)
        for meteor in meteor_hit_list:
            scare+=meteor.point
            player.shieldPoint -=1
        


        
    

#"""KOLISION DETECT WITH METEOR / Kolision detect player with meteor when shield is off"""
    
    else:
        meteor_hit_list = pygame.sprite.spritecollide(player,meteor_list,True)
        if len(meteor_hit_list) == 1:    #IF detect colision player have -1 live , POSITION meteors is CHANGED!
            player.live -=1
            """changeing meteor position when hit player"""
            if level == 0:
                for meteor in meteor_list:
                    meteor.rect.x = random.randrange(screen_width)-100
                    z = random.choice(range(200))
                    meteor.rect.y = -z
            
            meteor.update()



           
            """!!!!!!!!!!!!!END GAME"""
    if player.live == 0:
        font = pygame.font.Font(None, 120) #when player died , size text
        text = font.render("END GAME",1,(255,255,255))
        pygame.Surface.convert_alpha(text)
        all_sprites_list.empty() # remove all sprites
        gameDisplay.fill(black)
        gameDisplay.blit(text,(200,300)) #writen end game on display
        gameExit = True           
            
  


    
    """draw all sprites"""
    all_sprites_list.draw(gameDisplay)





    """Drowing scares / player points"""
    font1 = pygame.font.Font(None, 30) #size player point/scares
    text1 = font1.render(str(scare),1,(255,255,255))
    gameDisplay.blit(text1,(400,20))



    """DRAWING pLAYER SHIELD POINTS"""
    if player.shieldPoint > 0:
        pygame.draw.rect(gameDisplay,blue,(30,560,player.shieldPoint,30))
    if player.shieldPoint == 0:
        player.shield_down()
        
   
            
    pygame.time.wait(8) #speed game


    
   

    pygame.display.flip() #updating display
   

   



pygame.time.wait(2000)
pygame.quit()
quit()
