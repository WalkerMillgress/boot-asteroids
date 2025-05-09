import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfeild import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        
        for drawed in drawable:
            drawed.draw(screen)


        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                return


        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()