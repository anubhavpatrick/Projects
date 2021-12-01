'''The main module for the game'''

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    "Master class to manage game play and assets"

    def __init__(self):#constructor
        """Initializa the game,create game resources"""
        pygame.init()

        #create settings object
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #surface created

        pygame.display.set_caption("Alien Invasion by Anubhav")
        
        self.ship=Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Helper method to control the response to mouse and keyboard event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship towards right
                    self.ship.moving_right=True
                elif event.key == pygame.K_LEFT:
                    #move the ship towards left
                    self.ship.moving_left=True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #stop moving the ship towards right
                    self.ship.moving_right=False
                elif event.key == pygame.K_LEFT:
                    #stop moving the ship towards left
                    self.ship.moving_left=False

    def _update_screen(self):
        """Helper method to update elements on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
                
