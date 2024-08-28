from circleshape import CircleShape
from constants import *
from random import uniform
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        angle = uniform(20, 50)
        random_angle_1 = self.velocity.rotate(angle)
        random_angle_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = random_angle_1 * 1.2

        new_asteroId_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroId_2.velocity = random_angle_2

        self.kill()
        