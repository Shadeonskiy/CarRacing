import pygame

def get_scale_ratio(img, win):
    return max((win.get_width() / img.get_width()), (win.get_height() / img.get_height()))

def scale_image(img, scale_ratio):
    new_size = round(img.get_width() * scale_ratio), round(img.get_height() * scale_ratio)
    return pygame.transform.scale(img, new_size)

# Rotate image around its center and display it
def blit_rotate_center(win, img, top_left, angle):
    rotated_image = pygame.transform.rotate(img, angle)
    new_rect = rotated_image.get_rect(center = img.get_rect(topleft=top_left).center)
    
    win.blit(rotated_image, new_rect.topleft)