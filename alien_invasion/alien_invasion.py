'''The main module for the game'''

import sys

import pygame

class AlienInvasion:
    "Master class to manage game play and assets"

    def __init__(self):#constructor
        """Initializa the game,create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800)) #surface created

        pygame.display.set_caption("Alien Invasion by Anubhav")

        self.bg_color = (230,230,230)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#when user closes the window
                    sys.exit()
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
                
