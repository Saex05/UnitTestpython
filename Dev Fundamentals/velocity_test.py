import unittest
from shooting import Position
from shooting import Velocity

class VelocityTest(unittest.TestCase):
    def test_create_velocity_with_two_positions(self):
        start_possition = Position()
        end_possition = Position(4,3)

        velocity = Velocity(start_possition, end_possition)

        self.assertIsNotNone(velocity)

    def test_magnitude_is_zero_if_start_and_end_positions_are_the_same(selt):
         position = Position(1,1)
         velocity = Velocity(position,position)
         selt.assertEqual(0,velocity.magnitude())

    def test_magnitud_of_velocity_is_given_by_pythagoras_theorem(self):
        start_position = Position()
        end_posotion = Position(4,3)

        velocity = Velocity(start_position, end_posotion)
        self.assertEqual(5, velocity.magnitude())
    def test_angle_of_velocity_is_45_if_X_and_Y_of_end_position_are_same(self):
        start_position = Position()
        end_posotion = Position(2, 2)

        velocity = Velocity(start_position, end_posotion)
        self.assertEqual(45, velocity.angle())

    def test_angle_of_velocity_is_determined_by_the_arctangent(self):
        start_position = Position()
        end_posotion = Position(3, 4)

        velocity = Velocity(start_position, end_posotion)
        self.assertTrue(velocity.angle()>45)
        self.assertTrue(velocity.angle()<90)


if __name__ == "__main__":
    unittest.main()


