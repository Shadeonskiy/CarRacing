import time
from random import randint


class GameInfo:
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        """
        Sets the next level after completing the previous race
        """
        self.level += 1
        self.started = False
        return randint(0, 5)

    def reset(self):
        """
        Resets current level
        """
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        """
        Check whether the game is over or not
        """
        return self.level > self.LEVELS

    def start_level(self):
        """
        Starts a new level and tracks the race time
        """
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        """
        Return current level time
        """
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)
