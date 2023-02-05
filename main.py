import pygame
import constants
from utils import scale_image
from spriteloader import SpriteSheet
from render import ObjectRenderer
import argparse

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Car Racing Game")

run = True
clock = pygame.time.Clock()

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mv', '--max_velocity', default=4, type=int, choices=range(1, 11), help="set max velocity for player car")
    parser.add_argument('--rv', '--rotation_velocity', default=4, type=int, choices=range(1, 6), help="set rotation velocity for player car")
    parser.add_argument('--cc', '--car_color', default="red", choices=["blue","red","green","yellow","purple"], help="choose player car color")
    args = parser.parse_args(['--mv', '4', '--rv', '2','--cc', 'yellow'])
    return args

if __name__ == "__main__":
    args = init_argparser()
    print(f'Player Car Characteristics\n'
          f'max velocity: {args.mv} px/s\n'
          f'rotation velocity: {args.rv} px/s\n'
          f'color: {args.cc}\n')

    cars_spritesheet = SpriteSheet("Cars", "Sprites")
    cars_spritesheet.get_sprites()
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
            WIN.blit(cars_spritesheet.all_sprites["red_car"][0], (170, 200))
        elif rotate_right: 
            WIN.blit(cars_spritesheet.all_sprites["red_car"][6], (170, 200))
        elif rotate_left:
            WIN.blit(cars_spritesheet.all_sprites["red_car"][4], (170, 200))
    
    pygame.quit()
    quit()

        
    