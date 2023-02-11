import pygame
import constants
from spriteloader import SpriteSheet
from render import ObjectRenderer
import argparse
from car import PlayerCar, ComputerCar
from random import randint

clock = pygame.time.Clock()
track_index = randint(0,5)
finish_index = randint(0,1)

class Game():

    def __init__(self):
        self.play = False
        self.init_argparser()
        self.WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

        # Init object renderer, that draws all the necessary images, except the car (Delete if necessary)
        self.object_renderer = ObjectRenderer(track_index, finish_index)

        # Init object, that stores car states (images of different states) (Delete if necessary)
        self.spritesheet_loader = SpriteSheet("Cars", "Sprites")
        self.car_sprites = self.spritesheet_loader.get_sprites()

        # Init cars
        self.player_car = PlayerCar(self.args.mv, self.args.rv, self.car_sprites, track_index)
        self.computer_car = ComputerCar(3, 4, self.car_sprites, constants.COMPUTER_CAR_PATHS[track_index], track_index)


    def init_argparser(self):
        """
        Argument parser from terminal to determine car characteristics. Parse arguments when passing arguments in command line (cmd)
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--mv', '--max_velocity', default=4, type=int, choices=range(1, 11), help="set max velocity for player car")
        parser.add_argument('--rv', '--rotation_velocity', default=4, type=int, choices=range(1, 6), help="set rotation velocity for player car")
        parser.add_argument('--cc', '--car_color', default="red", choices=["blue","red","green","yellow","purple"], help="choose player car color")
        self.args = parser.parse_args(['--mv', '4', '--rv', '4','--cc', 'yellow'])

    def display_car_characteristics(self):
        """
        Display car characteristics on the console after parsing them from the terminal 
        (Afterwards will be passed to the car object)
        """
        print(f'Player Car Characteristics\n'
            f'max velocity: {self.args.mv} px/s\n'
            f'rotation velocity: {self.args.rv} px/s\n'
            f'color: {self.args.cc}\n')

    def run(self):
        """
        Starts the game loop
        """
        play = True
        
        pygame.display.set_caption("Car Racing Game")
        self.display_car_characteristics()

        while play:
            clock.tick(constants.FPS)

            self.draw_objects()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    break
            
            self.move_player()
            self.computer_car.move()
            # self.get_pressed_points()

    def move_player(self):
        """
        Tracks the keys pressed by the user and then moves the player's car
        """
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            self.player_car.rotate(left=True)
            self.player_car.animation_left = True

        if keys[pygame.K_d]:
            self.player_car.rotate(right=True)
            self.player_car.animation_right = True
            
        if keys[pygame.K_w]:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.player_car.move_backward()

        if not moved:
            self.player_car.reduce_speed()
    
    def draw_objects(self):
        """
        Draw all objects on the screen (render level)
        """ 
        self.object_renderer.render(self.WIN)
        self.player_car.draw(self.WIN)
        self.computer_car.draw(self.WIN)
        pygame.display.update()
    
    def get_pressed_points(self):
        """
        Get the (x, y) position of the mouse after clicking in the specified area of the screen
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            self.computer_car.path.append(pos)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    quit()

        