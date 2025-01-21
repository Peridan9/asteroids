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
        ran = random.uniform(20,50)
        vec1 = self.velocity.rotate(ran)
        vec2 = self.velocity.rotate(-ran)
        nR = self.radius - ASTEROID_MIN_RADIUS
        as1 = Asteroid(self.position.x,self.position.y,nR)
        as2 = Asteroid(self.position.x,self.position.y,nR)
        as1.velocity = vec1 * 1.2
        as2.velocity = vec2 * 1.2

        