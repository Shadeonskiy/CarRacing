import sys
import os
import pytest

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


@pytest.mark.animation
class TestAnimation:

    @pytest.mark.parametrize(["vel", "animation_left", "animation_right", "sprite_index", "expected_index"],
                             [(4, True, False, 9, 4),
                              (4, False, True, 15, 6)])
    def test_update_sprite(self, playerCar, vel, animation_left, animation_right, sprite_index, expected_index):
        playerCar.current_sprite = 0
        playerCar.car_sprites = [
            [1, 2, 3, 4, 5, 6, 7, 8],
        ]

        playerCar.vel = vel
        playerCar.animation_left = animation_left
        playerCar.animation_right = animation_right
        playerCar.sprite_index = sprite_index
        playerCar.update_sprite()

        assert playerCar.sprite_index == expected_index
