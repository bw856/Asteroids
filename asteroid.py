import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # if asteroid is small, destroy
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        
        # else, split into two asteroids
        split_angle = random.uniform(20, 50)
        a1_vector = self.velocity.rotate(split_angle)
        a2_vector = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        a1 = Asteroid(x, y, new_radius)
        a2 = Asteroid(x, y, new_radius)

        a1.velocity = a1_vector * 1.2
        a2.velocity = a2_vector* 1.2
