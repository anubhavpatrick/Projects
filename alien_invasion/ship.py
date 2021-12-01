import pygame

class Ship:
    '''A class to manage the ship behavior'''

    def __init__(self, ai_game):#ai_game is instance of the current AlienInvasion Class
        '''Initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings #to access settings for current instance
        self.screen_rect = self.screen.get_rect()#get the rect attribute of screen surface

        #load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Placing the ship at the mid bottom
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Storing the x coordinate of ship in float
        self.x = float(self.rect.x)

        #ship movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+=self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:#x coordinate starts from 0
            self.x-=self.settings.ship_speed

        #update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        '''Draw the ship at the current location'''
        self.screen.blit(self.image, self.rect)
