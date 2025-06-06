import sys

from pygame.sprite import Group
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import pygame

from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatables, drawable)
    Asteroid.containers = (asteroids, updatables, drawable)
    AsteroidField.containers = (updatables)
    Shot.containers = (bullets, updatables, drawable)

    asteroidField = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        for asteroid in asteroids:
            if player.colliding(asteroid):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if bullet.colliding(asteroid):
                    bullet.kill()
                    asteroid.split()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
