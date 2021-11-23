'''A module that stores and updates all the game settings'''

class Settings:
    '''A class to store all the settings of the game'''

    def __init__(self):
        '''Initialize the default settings of the game'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
