import unittest
from car import ComputerCar

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = ComputerCar(3, 4, [])
        self.car.path = [(0, 0), (0, 5)]
        self.car.current_point = 1
        self.car.x = 0
        self.car.y = 0
        self.car.angle = 0
        self.car.rotation_vel = 5

    def test_calculate_angle(self):
        # Test when y_diff is 0
        self.car.path[self.car.current_point] = (5, 0)
        self.car.calculate_angle()
        self.assertEqual(self.car.angle, 5)

        # Test when target_y > self.y
        self.car.path[self.car.current_point] = (5, 5)
        self.car.calculate_angle()
        self.assertEqual(self.car.angle, 10)

        # Test when target_y <= self.y
        self.car.path[self.car.current_point] = (5, -5)
        self.car.calculate_angle()
        self.assertEqual(self.car.angle, 5)

if __name__ == '__main__':
    unittest.main()