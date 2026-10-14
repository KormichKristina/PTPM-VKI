import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from laba1 import calculate_triangle


class TestCalculateTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        result, coordinates = calculate_triangle(10, 10, 10)
        self.assertEqual(result, "равносторонний")

    def test_isosceles_triangle(self):
        result, coordinates = calculate_triangle(5, 5, 6)
        self.assertEqual(result, "равнобедренный")

    def test_scalene_triangle(self):
        result, coordinates = calculate_triangle(4, 5, 6)
        self.assertEqual(result, "разносторонний")

    def test_zero_side(self):
        result, coordinates = calculate_triangle(0, 5, 5)
        self.assertEqual(result, "не треугольник")

    def test_negative_side(self):
        result, coordinates = calculate_triangle(-3, 4, 5)
        self.assertEqual(result, "не треугольник")

    def test_invalid_triangle(self):
        result, coordinates = calculate_triangle(1, 2, 10)
        self.assertEqual(result, "не треугольник")

    def test_degenerate_triangle(self):
        result, coordinates = calculate_triangle(2, 3, 5)
        self.assertEqual(result, "не треугольник")

    def test_coordinates_count(self):
        result, coordinates = calculate_triangle(3, 4, 5)
        self.assertEqual(len(coordinates), 3)

    def test_first_vertex(self):
        result, coordinates = calculate_triangle(3, 4, 5)
        self.assertEqual(coordinates[0], (0, 0))

    def test_invalid_triangle_coordinates(self):
        result, coordinates = calculate_triangle(1, 2, 10)
        self.assertEqual(coordinates, [(-1, -1)] * 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)