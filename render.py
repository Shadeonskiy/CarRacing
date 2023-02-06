import pygame
from utils import scale_image, get_scale_ratio, blit_rotate_center
from os import listdir
from os.path import isfile, join
import constants
from random import randint
import time

# Class to render level and images
class ObjectRenderer():
    def __init__(self):
        self.track_index = randint(0,5)
        self.finish_index = randint(0,1)
        self.GRASS = pygame.image.load("images/Maps/map_tile.png")
        self.FINISH_LINE = pygame.image.load("images/Maps/finish_line.png")
        self.TRACKS = [pygame.image.load(f"images/Maps/Tracks/track_{i}.png") for i in range(1,7)]
        self.TRACK_BORDERS = [pygame.image.load(f"images/Maps/Borders/trackBorder_{i}.png") for i in range(1,7)]

    # Renders images in specified area or in the center of the screen
    def render(self, win):
        IMAGES = [(self.GRASS, constants.STANDARD_POS), (self.TRACKS[self.track_index], constants.STANDARD_POS), 
            (self.FINISH_LINE, constants.FINISH_LINE_POS[self.track_index]), (self.TRACK_BORDERS[self.track_index], constants.STANDARD_POS)]

        for img, pos in IMAGES:
            scale_ratio = get_scale_ratio(img, win)
            img = scale_image(img, scale_ratio)
            
            if pos == (0, 0):
                rect = img.get_rect(center = win.get_rect().center)
                win.blit(img, rect)

            elif pos in constants.FINISH_LINE_POS: 
                img = scale_image(img, 0.065)
                cropped = pygame.Surface((100, 20), pygame.SRCALPHA, 32)
                cropped.blit(img, (0, 0), (0, 16, 200, 20))
                blit_rotate_center(win, cropped, pos, constants.FINISH_LINE_ANGLES[self.track_index])

            else: win.blit(img, pos)