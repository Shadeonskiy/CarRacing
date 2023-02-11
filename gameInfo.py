import pygame
import math
import constants
import time 

class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.level_start_time = 0

    def next_level(self):
        self.level += 1

    def reset(self):
        self.level = 1
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.level_start_time = time.time()

    def get_level_time(self):
        return round(time.time() - self.level_start_time)
