import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # group containers
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create asteroidfield
    asteroid_field = AsteroidField()
    
    while(1):
        # close window functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # draw background
        screen.fill((0,0,0))

        # update sprites
        for sprite in updateable:
            sprite.update(dt)

        # player-asteroid collision check
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # shot-asteroid collision check
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.kill()

        # draw sprites
        for sprite in drawable:
            sprite.draw(screen)

        # refresh display
        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000


# ensures main() function is only called main.py is run directly
if __name__ =="__main__":
    main()