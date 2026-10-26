"""Black-box tests derived from the specification in src/pricing.py.

Techniques: equivalence partitioning (EP), boundary value analysis (BVA), error guessing.
Test IDs (TC-xx) match docs/TEST_CASES.md.
"""
import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pricing import final_total  # noqa: E402

D = Decimal


class VolumeDiscountBoundaries(unittest.TestCase):
    def test_tc01_to_tc08_boundaries(self):
        cases = [  # (id, subtotal, expected)
            ("TC-01 zero", 0, "0.00"),
            ("TC-02 just above zero", D("0.01"), "0.01"),
            ("TC-03 top of 0% band", D("99.99"), "99.99"),
            ("TC-04 lower bound of 5% band", 100, "95.00"),
            ("TC-05 mid 5% band", 300, "285.00"),
            ("TC-06 top of 5% band", D("499.99"), "474.99"),
            ("TC-07 lower bound of 10% band", 500, "450.00"),
            ("TC-08 large order", 10000, "9000.00"),
        ]
        for name, subtotal, expected in cases:
            with self.subTest(name):
                self.assertEqual(final_total(subtotal), D(expected))


class CouponRules(unittest.TestCase):
    def test_tc09_coupon_below_minimum_is_ignored(self):
        self.assertEqual(final_total(D("49.99"), "WELCOME10"), D("49.99"))

    def test_tc10_coupon_at_minimum(self):
        self.assertEqual(final_total(50, "WELCOME10"), D("45.00"))

    def test_tc11_coupon_stacks_after_volume_discount(self):
        self.assertEqual(final_total(100, "WELCOME10"), D("85.50"))   # 100 -> 95 -> 85.5
        self.assertEqual(final_total(500, "WELCOME10"), D("405.00"))  # 500 -> 450 -> 405

    def test_tc12_no_coupon_equals_none(self):
        self.assertEqual(final_total(120, None), final_total(120))


class InvalidInput(unittest.TestCase):
    def test_tc13_negative_subtotal(self):
        for value in (-1, D("-0.01"), -1000):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    final_total(value)

    def test_tc14_wrong_types(self):
        for value in ("abc", None, [], True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    final_total(value)

    def test_tc15_nan(self):
        with self.assertRaises(ValueError):
            final_total(float("nan"))

    def test_tc16_unknown_coupon(self):
        for code in ("welcome10", "WELCOME20", ""):
            with self.subTest(code=code):
                with self.assertRaises(ValueError):
                    final_total(200, code)

    def test_tc17_unknown_coupon_rejected_even_below_minimum(self):
        with self.assertRaises(ValueError):
            final_total(10, "FAKE")


class Rounding(unittest.TestCase):
    def test_tc18_half_up_rounding(self):
        self.assertEqual(final_total(D("100.10")), D("95.10"))   # 95.095 -> 95.10
        self.assertEqual(final_total(D("0.05")), D("0.05"))

    def test_tc19_float_input_accepted(self):
        self.assertEqual(final_total(250.0), D("237.50"))

    def test_tc20_decimal_input_accepted(self):
        self.assertEqual(final_total(D("500.00")), D("450.00"))


if __name__ == "__main__":
    unittest.main()
