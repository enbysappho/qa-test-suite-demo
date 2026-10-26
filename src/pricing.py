"""System under test: order total calculation with volume discount and coupon.

Specification
-------------
* subtotal must be a number >= 0, otherwise ValueError.
* Volume discount (applied first):  < 100 -> 0 %,  100 <= subtotal < 500 -> 5 %,  >= 500 -> 10 %.
* Coupon "WELCOME10" gives a further 10 % off the discounted amount, only when the ORIGINAL subtotal is >= 50.
  A coupon used below 50 is ignored (no error). Any other coupon code raises ValueError.
* The result is rounded to 2 decimals, half up.
"""
from decimal import ROUND_HALF_UP, Decimal

COUPON = "WELCOME10"


def final_total(subtotal, coupon=None) -> Decimal:
    if isinstance(subtotal, bool) or not isinstance(subtotal, (int, float, Decimal)):
        raise ValueError("subtotal must be a number")
    amount = Decimal(str(subtotal))
    if amount.is_nan() or amount < 0:
        raise ValueError("subtotal must be >= 0")
    if coupon is not None and coupon != COUPON:
        raise ValueError(f"unknown coupon: {coupon!r}")

    if amount >= 500:
        rate = Decimal("0.10")
    elif amount >= 100:
        rate = Decimal("0.05")
    else:
        rate = Decimal("0")
    total = amount * (1 - rate)
    if coupon == COUPON and amount >= 50:
        total *= Decimal("0.90")
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
