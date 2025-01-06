import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    while(1):
        # close window functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # refresh screen
        screen.fill((0,0,0))
        pygame.display.flip()



# ensures main() function is only called main.py is run directly
if __name__ =="__main__":
    main()