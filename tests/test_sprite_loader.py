import sys
import os
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import constants
from spriteloader import SpriteSheet


@pytest.fixture
def car_imgs():
    spritesheet = SpriteSheet("Cars", "Sprites")
    spritesheet.width = constants.SPRITE_W
    spritesheet.height = constants.SPRITE_H

    return spritesheet


@pytest.fixture
def border_imgs():
    spritesheet = SpriteSheet("Maps", "Borders")
    spritesheet.width = constants.SPRITE_W
    spritesheet.height = constants.SPRITE_H

    return spritesheet


@pytest.mark.parametrize("spritesheet, expected_path, expected_images",
                         [("car_imgs", os.path.join("images", "Cars", "Sprites"),
                           ['red_car.png', 'purple_car.png', 'yellow_car.png', 'green_car.png', 'blue_car.png']),
                          ("border_imgs", os.path.join("images", "Maps", "Borders"),
                           ['trackBorder_1.png', 'trackBorder_2.png', 'trackBorder_3.png', 'trackBorder_4.png', 'trackBorder_5.png', 'trackBorder_6.png'])])
def test_load_sprite_sheets(spritesheet, expected_path, expected_images, request):
    spritesheet = request.getfixturevalue(spritesheet)
    spritesheet.load_sprite_sheets()
    assert spritesheet.path == expected_path
    assert set(spritesheet.images) == set(expected_images)
