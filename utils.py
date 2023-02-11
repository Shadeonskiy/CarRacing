import pygame
import math

def get_scale_ratio(img, win):
    if (img.get_width() > win.get_width() & img.get_height() < win.get_height()) | \
        (img.get_height() > win.get_height() & img.get_width() < win.get_width()):
        return min((win.get_width() / img.get_width()), (win.get_height() / img.get_height()))
        
    return max((win.get_width() / img.get_width()), (win.get_height() / img.get_height()))

def scale_image(img, scale_ratio):
    scale_ratio = math.fabs(scale_ratio)
    new_size = round(img.get_width() * scale_ratio), round(img.get_height() * scale_ratio)
    return pygame.transform.scale(img, new_size)


def blit_rotate_center(win, img, top_left, angle): 
    """
    Rotate image around its center and display it
    """
    rotated_image = pygame.transform.rotate(img, angle)
    new_rect = rotated_image.get_rect(center = img.get_rect(topleft=top_left).center)
    
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))