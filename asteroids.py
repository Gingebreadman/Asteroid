import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def split(self):
        # Always destroy the current asteroid
        self.kill()

        # If this asteroid is already the smallest size, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event
        log_event("asteroid_split")

        # Pick a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors rotated in opposite directions
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        # Compute the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Make them move faster (1.2x)
        a1.velocity = vel1 * 1.2
        a2.velocity = vel2 * 1.2

    def update(self, dt):
        # Move in a straight line
        self.position += self.velocity * dt

