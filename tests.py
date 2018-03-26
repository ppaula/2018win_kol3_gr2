import unittest
from plane import Plane
from environment import Environment

class TestPlane(unittest.TestCase):

    def test_origin(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.origin, "NYC")

    def test_dest(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.destination, "LA")

    def test_angle(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.angle, 0.0)

    def test_tilt_corr_counter(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.tilt_corr_counter, 0)

    def test_max_angle(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.max_angle, 15)

    def test_min_angle(self):
        test_plane = Plane("NYC", "LA")
        self.assertEqual(test_plane.min_angle, -15)

    def test_dictionary_ok(self):
        test_plane1 = Plane("NYC", "LA")
        test_plane2 = Plane("NYC", "LA")
        test_plane3 = Plane("NYC", "LA")
        env = Environment()
        env.add_plane(test_plane1, "plane1")
        env.add_plane(test_plane2, "plane2")
        env.add_plane(test_plane3, "plane3")
        self.assertTrue(len(env.planes) == 3)

    def test_dictionary_not_ok(self):
        test_plane1 = Plane("NYC", "LA")
        test_plane2 = Plane("NYC", "LA")
        test_plane3 = Plane("NYC", "LA")
        env = Environment()
        env.add_plane(test_plane1, "plane1")
        env.add_plane(test_plane2, "plane2")
        env.add_plane(test_plane3, "plane2")
        self.assertFalse(len(env.planes) == 3)

    def test_dictionary_same_planes_ok(self):
        test_plane1 = Plane("NYC", "LA")
        env = Environment()
        env.add_plane(test_plane1, "plane1")
        env.add_plane(test_plane1, "plane2")
        env.add_plane(test_plane1, "plane3")
        self.assertTrue(len(env.planes) == 3)

    def test_dictionary_same_planes_not_ok(self):
        test_plane1 = Plane("NYC", "LA")
        env = Environment()
        env.add_plane(test_plane1, "plane1")
        env.add_plane(test_plane1, "plane2")
        env.add_plane(test_plane1, "plane2")
        self.assertFalse(len(env.planes) == 3)


