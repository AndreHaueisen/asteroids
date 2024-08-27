import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable in updatables:
            updatable.update(dt)
            
        screen.fill((0,0,0))
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # time passed since last frame in seconds
        dt = clock.tick(FPS)/1000

if __name__ == "__main__":
    main()
