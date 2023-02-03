import pygame
import constants
from utils import scale_image
from spriteloader import SpriteSheet

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Racing Game!")

GRASS = scale_image(pygame.image.load("images/Maps/map_tile.png"), 0.3)
TRACK = scale_image(pygame.image.load("images/Maps/Tracks/track_1.png"), 0.44)

run = True
clock = pygame.time.Clock()
rotate = False
if __name__ == "__main__":
    sprite_sheet = SpriteSheet("Cars", "Sprites")
    sprite_sheet.get_sprites()
    
    while run:
        clock.tick(constants.FPS)
        pygame.display.update()

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        rotate = False
        if keys[pygame.K_a]:
            rotate = True

        WIN.blit(GRASS, (0,0))
        WIN.blit(TRACK, (-50,-50))

        if not rotate:
            WIN.blit(sprite_sheet.all_sprites["red_car"][0], (0,0))
        else: 
            WIN.blit(sprite_sheet.all_sprites["red_car"][5], (0,0))
    
    pygame.quit()

        
    