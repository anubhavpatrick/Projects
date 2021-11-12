import pygame

class Ship:
    '''A class to manage the ship behavior'''

    def __init__(self, ai_game):#ai_game is instance of the current AlienInvasion Class
        '''Initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()#get the rect attribute of screen surface

