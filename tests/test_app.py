import unittest
import tkinter as tk
import math


class TestColor3DApp(unittest.TestCase):

    def test_math_module(self):
        """Check that the math module works."""
        self.assertEqual(round(math.sin(0), 5), 0)
        self.assertEqual(round(math.cos(0), 5), 1)

    def test_3d_rotation(self):
        """Test a basic 3D rotation."""
        x = 100
        z = 0
        angle = math.radians(90)

        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = x * math.sin(angle) + z * math.cos(angle)

        self.assertAlmostEqual(new_x, 0, places=5)
        self.assertAlmostEqual(new_z, 100, places=5)

    def test_tkinter(self):
        """Check that Tkinter can create a window."""
        root = tk.Tk()
        root.withdraw()

        self.assertIsNotNone(root)

        root.destroy()


if __name__ == "__main__":
    unittest.main()
