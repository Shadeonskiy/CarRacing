import pygame

def scale_image(img, scale_ratio):
    new_size = round(img.get_width() * scale_ratio), round(img.get_height() * scale_ratio)
    return pygame.transform.scale(img, new_size)