import sys

import pygame

from settingsbs import Settings
from character import Character

class BlueSky:
    """Make a game with a blue background"""

    def __init__(self):
        """Initialize the game, and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

        #Set background color to blue
        self.bg_color = (self.settings.bg_color)

        #initialize character bmp
        self.character = Character(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the game window background blue
            self.screen.fill(self.bg_color)
            self.character.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance and run the game
    bs = BlueSky()
    bs.run_game()