import pygame

class Rocket:
    def __init__(self, rocket_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start the rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Set a decimal value for the rocket's horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the rocket's position"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        #Update rect object from position attributes.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)