import pygame
import constants
from utils import scale_image
from spriteloader import SpriteSheet
from render import ObjectRenderer

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Racing Game!")

run = True
clock = pygame.time.Clock()

if __name__ == "__main__":
    sprite_sheet = SpriteSheet("Cars", "Sprites")
    sprite_sheet.get_sprites()
    objects = ObjectRenderer()

    while run:
        clock.tick(constants.FPS)
        pygame.display.update()

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        rotate_left = False
        rotate_right = False
        if keys[pygame.K_a]:
            if rotate_right:
                rotate_right = False
            rotate_left = True
        if keys[pygame.K_d]:
            if rotate_left:
                rotate_left = False
            rotate_right = True

        objects.render(WIN)

        if not rotate_left | rotate_right:
            WIN.blit(sprite_sheet.all_sprites["red_car"][0], (170, 200))
        elif rotate_right: 
            WIN.blit(sprite_sheet.all_sprites["red_car"][6], (170, 200))
        elif rotate_left:
            WIN.blit(sprite_sheet.all_sprites["red_car"][4], (170, 200))
    
    pygame.quit()
    quit()

        
    