import pygame

class Character:
    """A class to make a character"""

    def __init__(self, bs_game):
        """Initialize the character and set its starting position"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/kaneki.bmp')
        self.rect = self.image.get_rect()

        # Start the new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)