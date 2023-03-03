import sys
import os
import pytest
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from car import PlayerCar


@pytest.fixture
def playerCar():
    """
    Return a player car object instance for the testing sessions
    """
    playerCar = PlayerCar(4, 4)
    playerCar.angle = 15
    playerCar.x, playerCar.y = (400, 400)

    return playerCar


@pytest.mark.moving
class TestMoving:

    @pytest.mark.parametrize(["vel", "expected_x", "expected_y", "expected_vel"],
                             [(3, 400 - math.sin(math.radians(15)) * 3.1, 400 - math.cos(math.radians(15)) * 3.1, 3.1),
                              (-0.1, 400, 400, 0)])
    def test_move_forward(self, playerCar, vel, expected_x, expected_y, expected_vel):
        playerCar.vel = vel
        playerCar.move_forward()
        assert playerCar.x == expected_x
        assert playerCar.y == expected_y
        assert playerCar.vel == expected_vel

    @pytest.mark.parametrize(["vel", "expected_x", "expected_y", "expected_vel"],
                             [(-2, 400 - math.sin(math.radians(15)) * -2, 400 - math.cos(math.radians(15)) * -2, -2),
                              (0.1, 400, 400, 0)])
    def test_move_backward(self, playerCar, vel, expected_x, expected_y, expected_vel):
        playerCar.vel = vel
        playerCar.move_backward()
        assert playerCar.x == expected_x
        assert playerCar.y == expected_y
        assert playerCar.vel == expected_vel


@pytest.mark.events
class TestEvents:

    @pytest.mark.parametrize(["vel", "expected_x", "expected_y", "expected_vel"],
                             [(3, 400 - math.sin(math.radians(15)) * 2.95, 400 - math.cos(math.radians(15)) * 2.95, 2.95),
                              (0, 400, 400, 0)])
    def test_reduce_speed(self, playerCar, vel, expected_x, expected_y, expected_vel):
        playerCar.vel = vel
        playerCar.reduce_speed()
        assert playerCar.x == expected_x
        assert playerCar.y == expected_y
        assert playerCar.vel == expected_vel

    @pytest.mark.parametrize(["vel", "expected_vel"], [(-2, 1), (2, -1), (4, -2), (0, 0)])
    def test_bounce(self, playerCar, vel, expected_vel):
        playerCar.vel = vel
        playerCar.bounce()
        assert playerCar.vel == expected_vel
