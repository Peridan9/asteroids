from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Asteroid big enough to be split

        # random direction to move in given range
        ran = random.uniform(20,50)
        
        # create two velcoties based on the new diraction
        vec1 = self.velocity.rotate(ran)
        vec2 = self.velocity.rotate(-ran)

        # new radius to the asteroid
        nR = self.radius - ASTEROID_MIN_RADIUS

        # creating two new asteroids
        as1 = Asteroid(self.position.x,self.position.y,nR)
        as2 = Asteroid(self.position.x,self.position.y,nR)

        # changing their direction and speed
        as1.velocity = vec1 * 1.2
        as2.velocity = vec2 * 1.2

        