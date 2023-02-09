import pygame
import constants
from spriteloader import SpriteSheet
from render import ObjectRenderer
import argparse
from car import PlayerCar, ComputerCar
from random import randint

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Car Racing Game")

track_index = randint(0,5)
finish_index = randint(0,1)

def draw(win : pygame.Surface, objects, player_car, computer_car):
    objects.render(win)
    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()

run = True
clock = pygame.time.Clock()
player_car = PlayerCar(3, 3, track_index)
computer_car = ComputerCar(3, 4, constants.COMPUTER_CAR_PATHS[track_index], track_index)

def init_argparser():
    """
    Argument parser from terminal to determine car characteristics. Parse arguments when passing arguments in command line (cmd)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--mv', '--max_velocity', default=4, type=int, choices=range(1, 11), help="set max velocity for player car")
    parser.add_argument('--rv', '--rotation_velocity', default=4, type=int, choices=range(1, 6), help="set rotation velocity for player car")
    parser.add_argument('--cc', '--car_color', default="red", choices=["blue","red","green","yellow","purple"], help="choose player car color")
    args = parser.parse_args(['--mv', '4', '--rv', '2','--cc', 'yellow'])
    return args

def get_current_points():
    """
    Get the (x, y) position of the mouse after clicking in the specified area of the screen
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        computer_car.path.append(pos)

if __name__ == "__main__":
    # Display car characteristics on the console after parsing them from the terminal 
    # (Afterwards will be passed to the car object)
    args = init_argparser()
    print(f'Player Car Characteristics\n'
          f'max velocity: {args.mv} px/s\n'
          f'rotation velocity: {args.rv} px/s\n'
          f'color: {args.cc}\n')

    # Init object, that stores car states (images of different states) (Delete if necessary)
    cars_spritesheet = SpriteSheet("Cars", "Sprites")
    cars_spritesheet.get_sprites()
    # Init object renderer, that draws all the necessary images, except the car (Delete if necessary)
    objects = ObjectRenderer(track_index, finish_index)

    # Main game loop
    while run:
        clock.tick(constants.FPS)

        draw(WIN, objects, player_car, computer_car)
        pygame.display.update()
        # Testing function of changing car images when a certain key is pressed (Delete if necessary)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            get_current_points()
            
        # the ability to move and rotate car using keys 
        if keys[pygame.K_a]:
            player_car.rotate(left=True)

        if keys[pygame.K_d]:
            player_car.rotate(right=True)

        if keys[pygame.K_w]:
            moved = True
            player_car.move_forward()

        if keys[pygame.K_s]:
            moved = True
            player_car.move_backward()
        
        computer_car.move()

    print(computer_car.path)

    pygame.quit()
    quit()

        
    