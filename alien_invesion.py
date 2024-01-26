import sys
import pygame
from settings import Settings

class AlienInvasion:
    "class for  manage game and behaviour"
    def __init__(self) -> None:
        "iitialize game and create resources"
        pygame.init()
         # it is describe time somthing( i don't know)
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        # set display and it's size.
        # self.screen is a var. for store the diplay its not mandatory..!!
        # self.screen=pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Alien Invasion")
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))

        # Set the background color.
        self.bg_color = (230,230,230)
        # (255,000,000)->red     (230,230,230)->white
       
        
    
    def run_game(self):
        "strat the main loop for the game"
        while True:
            # whatch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            self.screen.fill(self.settings.bg_color)
            
            # Make the most recently drawn screen visible:
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make the game instance and run the game.
    ai=AlienInvasion()
    ai.run_game()