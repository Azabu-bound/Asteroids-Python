import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
  print("Starting asteroids!")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  dt = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for obj in updatable:
      obj.update(dt)

    for asteroid in asteroids:
      if asteroid.collision_check(player):
        print("Game Over!")
        sys.exit()

    screen.fill("black")

    for obj in drawable:
      obj.draw(screen)
 
    pygame.display.flip()
    
    # limit the fps to 60
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()