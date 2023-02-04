import pygame
from utils import scale_image, get_scale_ratio
from os import listdir
from os.path import isfile, join
import constants
import time

GRASS = pygame.image.load("images/Maps/map_tile.png")
TRACK = pygame.image.load("images/Maps/Tracks/track_1.png")
IMAGES = [(GRASS, constants.STANDARD_POS), (TRACK, constants.STANDARD_POS)]

class ObjectRenderer():
    def __init__(self):
        self.images = IMAGES

    # Loads images from specified directory
    def load_images(self):
        pass
    
    # Renders images in specified area or in the center of the screen
    def render(self, win):
        for img, pos in self.images:
            scale_ratio = get_scale_ratio(img, win)
            img = scale_image(img, scale_ratio)
            if pos == (0, 0):
                rect = img.get_rect(center = win.get_rect().center)
                win.blit(img, rect)
            else: win.blit(img, pos)