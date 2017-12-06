import unittest
from shooting import Projectile, Position, Velocity

class projectileTest(unittest.TestCase):
    def test_projectile_is_create_with_inital_position(self):
        projectile = Projectile(Position(5,25))
        self.assertTrue(isinstance(projectile,Projectile))

    def test_position_changes_when_projectile_is_shoot(self):

        initial_position = Position()
        projectile = Projectile(Position())
        velocity = Velocity(Position(), Position(3, 5))

        projectile.shoot(velocity)

        self.assertTrue(isinstance(projectile.position()))
        self.assertNotEquals(initial_position(), projectile.position())




if __name__ == "__main__":
    unittest.main()