import sys
import os
import pygame

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from utils import blit_rotate_center, scale_image, get_scale_ratio

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.image = pygame.image.load("images/Maps/Tracks/track_1.png")
        self.scale_ratio = 0.5
        self.win = pygame.display.set_mode((1000, 1000)) 
        self.angle = 45

    def test_scale_image(self):
        scaled_image = scale_image(self.image, self.scale_ratio)
        self.assertEqual((scaled_image.get_width(), scaled_image.get_height()), (800, 800))
        
        scaled_image = scale_image(self.image, -self.scale_ratio)
        self.assertEqual((scaled_image.get_width(), scaled_image.get_height()), (800, 800))

        scaled_image = scale_image(self.image, self.scale_ratio * 2)
        self.assertEqual((scaled_image.get_width(), scaled_image.get_height()), (1600, 1600))

    def test_get_scale_ratio(self):
        # find out whether it gives ratio to fit window size
        scale_ratio = get_scale_ratio(self.image, self.win)
        self.assertEqual(scale_ratio, 0.625)
        
        # if image size isn't responsive square, it should take minimal aspect ratio
        img = pygame.Surface((1600, 900))
        scale_ratio = get_scale_ratio(img, self.win)
        self.assertEqual(scale_ratio, 0.625)

if __name__ == "__main__":
    unittest.main()