import pygame
import math
import constants
from utils import scale_image, blit_rotate_center

RED_CAR = scale_image(pygame.image.load("images/Cars/Red Car/carRed_0.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("images/Cars/Green Car/carGreen_0.png"), 0.55)

class Car:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move_way_back()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def move_way_back(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y += vertical
        self.x += horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class PlayerCar(Car):
    IMG = RED_CAR
    START_POS = (180, 200)
    def __init__(self, max_vel, rotation_vel, track_index=1, finish_index=0):
        self.START_POS = constants.PLAYER_CAR_START_POS[track_index]
        super().__init__(max_vel, rotation_vel)
        self.angle = constants.FINISH_LINE_ANGLES[track_index]

class ComputerCar(Car):
    IMG = GREEN_CAR
    START_POS = (150, 200)

    def __init__(self, max_vel, rotation_vel, path = [], track_index=1, finish_index=0):
        self.START_POS = constants.COMPUTER_CAR_START_POS[track_index]
        super().__init__(max_vel, rotation_vel)
        self.angle = constants.FINISH_LINE_ANGLES[track_index]
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win):
        super().draw(win)
        self.draw_points(win)
    
    def move(self):
        # check this to ensure that we won't get an index error when trying to move towards the point that doesn't exist
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            radian_angle = math.pi/2
        else:
            radian_angle = math.atan(x_diff/y_diff)
        
        if target_y > self.y:
            radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360
        
        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))
    
    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1