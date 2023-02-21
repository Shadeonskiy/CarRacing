import pygame
import constants
from utils import scale_image
from os import listdir
from os.path import isfile, join


class SpriteSheet():
    all_sprites = {}
    path = ""
    images = []

    def __init__(self, dir1, dir2):
        self.width = constants.SPRITE_W
        self.height = constants.SPRITE_H
        self.dir1 = dir1
        self.dir2 = dir2

    def load_sprite_sheets(self):
        """
        Loads every single file that is inside specified directory
        """
        # Specifying path to the spritesheets directory
        self.path = join("images", self.dir1, self.dir2)
        # Loading every single file that is inside specified directory
        self.images = [file for file in listdir(self.path)
                       if isfile(join(self.path, file))]

    def get_sprites(self):
        """
        Extracts sprites from the spritesheet to dict
        """
        self.load_sprite_sheets()

        # Getting all spritesheets
        for image in self.images:
            sprite_sheet = pygame.image.load(join(self.path, image))\
                                       .convert_alpha()

            # Split spritesheet into single sprites
            sprites = []
            for i in range(sprite_sheet.get_width() // self.width):
                surface = pygame.Surface((self.width, self.height),
                                         pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * self.width, 0, self.width, self.height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(scale_image(surface, 0.5))

            self.all_sprites[image.replace(".png", "")] = sprites

        return self.all_sprites
