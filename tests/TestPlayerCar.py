import sys
import os
import pygame
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

pygame.display.set_mode((1,1))

import unittest
from car import PlayerCar

class TestCar(unittest.TestCase):
    def setUp(self):
        self.playerCar = PlayerCar(4, 4)
        self.playerCar.vel = 3
        self.playerCar.angle = 15
        self.playerCar.x, self.playerCar.y = (400, 400)

    def test_move(self):
        x = 400 - math.sin(math.radians(15)) * 3.1
        y = 400 - math.cos(math.radians(15)) * 3.1
        self.playerCar.move_forward()
        self.assertAlmostEqual(self.playerCar.x, x)
        self.assertAlmostEqual(self.playerCar.y, y)
        self.assertEqual(self.playerCar.vel, 3.1)

        self.playerCar.vel = -0.1
        self.playerCar.x = 400
        self.playerCar.y = 400
        self.playerCar.move_forward()
        self.assertAlmostEqual(self.playerCar.x, 400)
        self.assertAlmostEqual(self.playerCar.y, 400)

    def test_reduce_speed(self):
        x = 400 - math.sin(math.radians(15)) * 2.95
        y = 400 - math.cos(math.radians(15)) * 2.95
        self.playerCar.reduce_speed()
        self.assertAlmostEqual(self.playerCar.x, x)
        self.assertAlmostEqual(self.playerCar.y, y)
        self.assertEqual(self.playerCar.vel, 2.95)

        self.playerCar.vel = 0
        self.playerCar.x = 400
        self.playerCar.y = 400
        self.playerCar.reduce_speed()
        self.assertAlmostEqual(self.playerCar.x, 400)
        self.assertAlmostEqual(self.playerCar.y, 400)


    pass

if __name__ == "__main__":
    unittest.main()