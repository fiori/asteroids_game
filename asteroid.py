import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_SPEED


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.spawn()


    def spawn(self):
        random_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * 1.2





