from asyncio import events
import pygame
import constants
from spriteloader import SpriteSheet
from render import ObjectRenderer
import argparse
from car import PlayerCar, ComputerCar
from random import randint
from gameInfo import GameInfo
from utils import blit_text_center
import button

clock = pygame.time.Clock()
track_index = randint(0, 5)
finish_index = randint(0, 1)

pygame.font.init()


class Game():

    def __init__(self):
        self.running = False
        self.init_argparser()
        self.WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.MAIN_FONT = pygame.font.SysFont("comicsans", 24)

        # Init object renderer, that draws all the necessary images,
        # except the car (Delete if necessary)
        self.object_renderer = ObjectRenderer(track_index, finish_index)

        # Init object, that stores car states (images of different states)
        # (Delete if necessary)
        self.spritesheet_loader = SpriteSheet("Cars", "Sprites")
        self.car_sprites = self.spritesheet_loader.get_sprites()

        # Init cars
        self.current_sprite = "purple_car"
        self.player_car = PlayerCar(self.args.mv, self.args.rv,
                                    self.car_sprites, self.current_sprite,
                                    track_index)
        self.computer_car = ComputerCar(3, 4, self.car_sprites,
                                        constants.COMPUTER_CAR_PATHS[track_index],
                                        track_index)

        # Init game Info
        self.game_info = GameInfo()

        # Menu vars
        self.menu = False
        self.car_menu = False
        self.menu_state = 'main'

        # resume button
        self.resume_img = button.createButtonImage("images/Buttons/button_resume.png")
        self.resume_button = button.createButton(self.resume_img, -100)

        # choose car button
        self.choose_car_img = button.createButtonImage("images/Buttons/choose_car.png")
        self.choose_car_button = button.createButton(self.choose_car_img, 0)

        # quit button
        self.quit_img = button.createButtonImage("images/Buttons/button_quit.png")
        self.quit_button = button.createButton(self.quit_img, 100)

        # back button car menu
        self.back_img = button.createButtonImage("images/Buttons/button_back.png")
        self.back_button = button.createButton(self.back_img, 200)

        # car color buttons
        # red
        self.red_car_img = button.createButtonImage("images/Buttons/Color buttons/red_btn.png")
        self.color_button_red = button.createButton(self.red_car_img, 100)

        # blue
        self.blue_car_img = button.createButtonImage("images/Buttons/Color buttons/blue_btn.png")
        self.color_button_blue = button.createButton(self.blue_car_img, 0)

        # purple
        self.purple_car_img = button.createButtonImage("images/Buttons/Color buttons/purple_btn.png")
        self.color_button_purple = button.createButton(self.purple_car_img, -100)

        # yellow
        self.yellow_car_img = button.createButtonImage("images/Buttons/Color buttons/yellow_btn.png")
        self.color_button_yellow = button.createButton(self.yellow_car_img, -200)

    def init_argparser(self):
        """
        Argument parser from terminal to determine car characteristics.
        Parse arguments when passing arguments in command line (cmd)
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--mv', '--max_velocity', default=4,
                            type=int, choices=range(1, 11),
                            help="set max velocity for player car")
        parser.add_argument('--rv', '--rotation_velocity', default=4,
                            type=int, choices=range(1, 6),
                            help="set rotation velocity for player car")
        parser.add_argument('--cc', '--car_color', default="red",
                            choices=["blue", "red", "green", "yellow", "purple"],
                            help="choose player car color")
        self.args = parser.parse_args(['--mv', '4', '--rv', '4', '--cc', 'yellow'])

    def display_car_characteristics(self):
        """
        Display car characteristics on the console after parsing
        them from the terminal (Afterwards will be passed to the car object)
        """
        print(f'Player Car Characteristics\n'
              f'max velocity: {self.args.mv} px/s\n'
              f'rotation velocity: {self.args.rv} px/s\n'
              f'color: {self.args.cc}\n')

    def run(self):
        """
        Starts the game loop
        """
        self.running = True

        pygame.display.set_caption("Car Racing Game")
        self.display_car_characteristics()

        while self.running:
            clock.tick(constants.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    self.menu = False

            self.draw_objects()

            while not self.game_info.started:
                blit_text_center(self.WIN, self.MAIN_FONT,
                                 f"Press any key to start level {self.game_info.level}!")
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    if event.type == pygame.KEYDOWN:
                        self.game_info.start_level()

            while self.menu:

                self.WIN.fill((52, 78, 91))

                if self.menu_state == 'main':
                    if self.resume_button.draw(self.WIN):
                        self.menu = False

                    if self.choose_car_button.draw(self.WIN):
                        self.menu_state = 'car'

                    if self.quit_button.draw(self.WIN):
                        self.running = False

                # sub menu car menu
                if self.menu_state == 'car':
                    if self.back_button.draw(self.WIN):
                        self.menu_state = 'main'

                    if self.color_button_red.draw(self.WIN):
                        self.player_car.current_sprite = 'red_car'

                    if self.color_button_purple.draw(self.WIN):
                        self.player_car.current_sprite = 'purple_car'

                    if self.color_button_yellow.draw(self.WIN):
                        self.player_car.current_sprite = 'yellow_car'

                    if self.color_button_blue.draw(self.WIN):
                        self.player_car.current_sprite = 'blue_car'

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                    if event.type == pygame.KEYDOWN:
                        self.menu = False

            self.move_player()
            self.computer_car.move()
            self.handle_collision()
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

        if keys[pygame.K_ESCAPE]:
            self.menu = True

        if not moved:
            self.player_car.reduce_speed()

    def handle_collision(self):
        """
        Process cars collision with the track and finish line (When POI isn't none)
        """
        TRACK_BORDER_MASK, TRACK_POS = self.object_renderer.get_border_mask(self.WIN)
        if self.player_car.collide(TRACK_BORDER_MASK, *TRACK_POS) is not None:
            self.player_car.bounce()

        FINISH_MASK, FINISH_POS = self.object_renderer.get_finish_mask(self.WIN)
        player_finish_poi = self.player_car.collide(FINISH_MASK,
                                                    *FINISH_POS)
        if player_finish_poi is not None:
            if player_finish_poi[1] == 0:
                self.player_car.bounce()
            else:
                new_track_index = self.game_info.next_level()
                self.object_renderer.track_index = new_track_index
                self.player_car.track_index = new_track_index
                self.computer_car.track_index = new_track_index
                self.player_car.next_level()
                self.computer_car.next_level(self.game_info.level)

        computer_finish_poi = self.computer_car.collide(FINISH_MASK,
                                                        *FINISH_POS)
        if computer_finish_poi is not None:
            blit_text_center(self.WIN, self.MAIN_FONT, "You lost!")
            pygame.display.update()
            pygame.time.wait(5000)
            self.game_info.reset()
            self.player_car.reset()
            self.computer_car.reset()

    def draw_objects(self):
        """
        Draw all objects on the screen (render level)
        """
        self.object_renderer.render(self.WIN)

        level_text = self.MAIN_FONT.render(f"Level {self.game_info.level}",
                                           1, (255, 255, 255))
        self.WIN.blit(level_text, (10, constants.HEIGHT - level_text.get_height() - 70))

        time_text = self.MAIN_FONT.render(f"Time: {self.game_info.get_level_time()}s",
                                          1, (255, 255, 255))
        self.WIN.blit(time_text, (10, constants.HEIGHT - time_text.get_height() - 40))

        vel_text = self.MAIN_FONT.render(f"Vel: {round(self.player_car.vel, 1)}px/s",
                                         1, (255, 255, 255))
        self.WIN.blit(vel_text, (10, constants.HEIGHT - vel_text.get_height() - 10))

        self.player_car.draw(self.WIN)
        self.computer_car.draw(self.WIN)
        pygame.display.update()

    def get_pressed_points(self):
        """
        Get the (x, y) position of the mouse after clicking in the
        specified area of the screen
        """
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            self.computer_car.path.append(pos)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    quit()
