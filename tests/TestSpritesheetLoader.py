import sys
import os
import pygame

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

pygame.display.set_mode((1, 1))

import unittest
import constants
from spriteloader import SpriteSheet

images_expected_result = ['blue_car.png', 'green_car.png', 'purple_car.png', 'red_car.png', 'yellow_car.png']
sprites_expected_result = [8, 8, 8, 8, 8]

class TestSpriteSheet(unittest.TestCase):

    def setUp(self):
        self.spritesheet = SpriteSheet("Cars", "Sprites")
        self.spritesheet.width = constants.SPRITE_W
        self.spritesheet.height = constants.SPRITE_H

    def test_load_sprite_sheets(self):
        self.spritesheet.load_sprite_sheets()
        self.assertEqual(self.spritesheet.path, "images\Cars\Sprites")
        self.assertEqual(self.spritesheet.images, images_expected_result)

    def test_get_sprites(self):
        # sprites dictionary must have 5 keys and 8 sprite images for each key
        self.spritesheet.get_sprites()
        keys_amount = len(self.spritesheet.all_sprites.keys())
        values_amount = [len(self.spritesheet.all_sprites[i]) for i in self.spritesheet.all_sprites.keys()]
        self.assertEqual(keys_amount, 5)
        self.assertEqual(values_amount, sprites_expected_result)

    pass

if __name__ == "__main__":
    unittest.main()
