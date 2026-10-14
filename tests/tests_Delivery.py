import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from Delivery import calculate_delivery_cost


class TestCalculateDeliveryCost(unittest.TestCase):

    def test_standard_delivery(self):
        result = calculate_delivery_cost(2.0, 100, "обычный")
        self.assertEqual(result, (700, "2026-09-04"))

    def test_fragile_package(self):
        result = calculate_delivery_cost(2.0, 100, "хрупкий")
        self.assertEqual(result, (1000, "2026-09-04"))

    def test_dangerous_package(self):
        result = calculate_delivery_cost(2.0, 100, "опасный")
        self.assertEqual(result, (1700, "2026-09-04"))

    def test_medium_weight(self):
        result = calculate_delivery_cost(10.0, 100, "обычный")
        self.assertEqual(result, (840, "2026-09-04"))

    def test_heavy_package(self):
        result = calculate_delivery_cost(25.0, 100, "обычный")
        self.assertEqual(result, (1050, "2026-09-04"))

    def test_express_delivery(self):
        result = calculate_delivery_cost(
            2.0, 100, "обычный", True
        )
        self.assertEqual(result, (350, "2026-09-04"))

    def test_minimum_weight(self):
        result = calculate_delivery_cost(0.1, 1, "обычный")
        self.assertEqual(result, (205, "2026-09-04"))

    def test_invalid_weight(self):
        result = calculate_delivery_cost(0.05, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_invalid_distance(self):
        result = calculate_delivery_cost(2.0, 6000, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_invalid_package_type(self):
        result = calculate_delivery_cost(2.0, 100, "нестандартный")
        self.assertEqual(result, (-1, "0000-00-00"))


if __name__ == "__main__":
    unittest.main(verbosity=2)