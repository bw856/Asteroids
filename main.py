import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # clock
    clock = pygame.time.Clock()
    dt = 0

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while(1):
        # close window functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # draw background
        screen.fill((0,0,0))

        # draw player
        player.draw(screen)

        # update player
        player.update(dt)

        # refresh display
        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000


# ensures main() function is only called main.py is run directly
if __name__ =="__main__":
    main()