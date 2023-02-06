import pygame
import math
from utils import scale_image, blit_rotate_center

RED_CAR = scale_image(pygame.image.load("images/Cars/Red Car/carRed_0.png"), 0.55)

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
        

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)