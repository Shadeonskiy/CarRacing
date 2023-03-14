import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from car import ComputerCar


@pytest.mark.computer_car
class TestCar:

    @pytest.fixture
    def computer_car(self):
        car = ComputerCar(3, 4, [])
        car.path = [(0, 0), (0, 5)]
        car.current_point = 1
        car.x = 0
        car.y = 0
        car.angle = 0
        car.rotation_vel = 5

        return car

    @pytest.mark.parametrize("path, angle, expected_angle", [((5, 0), 0, 5),
                                                             ((5, 5), 5, 10),
                                                             ((5, -5), 10, 5),])
    def test_calculate_angle(self, computer_car, path, angle, expected_angle):
        # Test when y_diff is 0
        computer_car.path[computer_car.current_point] = path
        computer_car.angle = angle
        computer_car.calculate_angle()

        assert computer_car.angle == expected_angle
