import pygame
from utils import scale_image, get_scale_ratio, blit_rotate_center
import constants


# Class to render level and images
class ObjectRenderer():
    def __init__(self, track_index=0, finish_index=0):
        self.track_index = track_index
        self.finish_index = finish_index
        self.GRASS = pygame.image.load("images/Maps/map_tile.png")
        self.FINISH_LINE = pygame.image.load("images/Maps/finish_line.png")
        self.TRACKS = [pygame.image.load(f"images/Maps/Tracks/track_{i}.png")
                       for i in range(1, 7)]
        self.TRACK_BORDERS = [pygame.image
                              .load(f"images/Maps/Borders/trackBorder_{i}.png")
                              for i in range(1, 7)]

    def scale_win_size(self, img, win):
        scale_ratio = get_scale_ratio(img, win)
        return scale_image(img, scale_ratio)

    def render(self, win):
        """
        Renders images in specified area or in the center of the screen
        """
        IMAGES = [(self.GRASS, constants.STANDARD_POS),
                  (self.TRACKS[self.track_index], constants.STANDARD_POS),
                  (self.FINISH_LINE, constants.FINISH_LINE_POS[self.track_index]),
                  (self.TRACK_BORDERS[self.track_index], constants.STANDARD_POS)]

        for img, pos in IMAGES:
            img = self.scale_win_size(img, win)

            if pos == (0, 0):
                rect = img.get_rect(center=win.get_rect().center)
                win.blit(img, rect)

            elif pos in constants.FINISH_LINE_POS:
                img = scale_image(img, 0.5)
                cropped = pygame.Surface((100, 20), pygame.SRCALPHA, 32)
                cropped.blit(img, (0, 0), (0, 19, 200, 20))
                blit_rotate_center(win,
                                   cropped,
                                   pos,
                                   constants.FINISH_LINE_ANGLES[self.track_index])

            else:
                win.blit(img, pos)

    def get_border_mask(self, win):
        """
        Returns track border mask (Rect without transparent pixels)
        """
        track_border = self.scale_win_size(self.TRACK_BORDERS[self.track_index],
                                           win)
        TRACK_BORDER_MASK = pygame.mask.from_surface(track_border)
        return TRACK_BORDER_MASK, constants.STANDARD_POS

    def get_finish_mask(self, win):
        """
        Returns finish line mask
        """
        finish_line = scale_image(self.scale_win_size(self.FINISH_LINE, win),
                                  0.5)
        cropped = pygame.Surface((100, 20), pygame.SRCALPHA, 32)
        cropped.blit(finish_line, (0, 0), (0, 19, 200, 20))
        finish_line, pos = blit_rotate_center(win, cropped,
                                              constants.FINISH_LINE_POS[self.track_index],
                                              constants.FINISH_LINE_ANGLES[self.track_index])
        FINISH_MASK = pygame.mask.from_surface(finish_line)
        return FINISH_MASK, pos
