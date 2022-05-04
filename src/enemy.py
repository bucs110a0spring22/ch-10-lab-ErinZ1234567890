import pygame
import random
#from src import controller 
#from src.controller import getHeroX
#from src import hero
#from src.controller import hero
#from src.hero import rect
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        
        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    """
Enemies move randomly and cannot move completely out of bounds
    """
    def update(self):  
      
      if(self.rect.x > 600):
        self.rect.x += random.randint(-1,0)
      if(self.rect.x < 1):
        self.rect.x += random.randint(0,1)
      if(self.rect.y > 430):
        self.rect.y += random.randint(-1,0)
      if(self.rect.y < 1):
        self.rect.y += random.randint(0,1)
      self.rect.x += random.randint(-1, 1)
      self.rect.y += random.randint(-1, 1)


    """
dodge: allows the enemy to dodge an attack randomly. if attack is dodged, enemy does not die. otherwise, the attack is successful and the enemy is defeated
    """
    def dodge(self):
        if(random.randrange(3)):
            print("enemy took damage")
            return False
        else:
            print("enemy dodged")
        return True
