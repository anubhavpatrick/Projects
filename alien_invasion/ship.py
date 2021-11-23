import pygame

class Ship:
    '''A class to manage the ship behavior'''

    def __init__(self, ai_game):#ai_game is instance of the current AlienInvasion Class
        '''Initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()#get the rect attribute of screen surface

        #load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Placing the ship at the mid bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship at the current location'''
        self.screen.blit(self.image, self.rect)
