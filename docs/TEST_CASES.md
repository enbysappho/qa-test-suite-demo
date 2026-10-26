# Test cases: `final_total(subtotal, coupon=None)`

Note: decimal amounts such as 99.99 are passed as `Decimal` in the tests to avoid binary floating-point error; plain strings are rejected by design (TC-14).

Technique: **EP** = equivalence partitioning, **BVA** = boundary value analysis, **EG** = error guessing.

| ID | Technique | Input (subtotal, coupon) | Expected | Why |
|---|---|---|---|---|
| TC-01 | BVA | 0, none | 0.00 | lowest valid value |
| TC-02 | BVA | 0.01, none | 0.01 | smallest positive amount |
| TC-03 | BVA | 99.99, none | 99.99 | top of the 0 % band |
| TC-04 | BVA | 100, none | 95.00 | lower bound of the 5 % band |
| TC-05 | EP | 300, none | 285.00 | representative 5 % value |
| TC-06 | BVA | 499.99, none | 474.99 | top of the 5 % band |
| TC-07 | BVA | 500, none | 450.00 | lower bound of the 10 % band |
| TC-08 | EP | 10000, none | 9000.00 | large order |
| TC-09 | BVA | 49.99, WELCOME10 | 49.99 | coupon ignored below the 50 minimum |
| TC-10 | BVA | 50, WELCOME10 | 45.00 | coupon applies at the minimum |
| TC-11 | EP | 100 / 500, WELCOME10 | 85.50 / 405.00 | coupon stacks after the volume discount |
| TC-12 | EP | 120, None | same as no coupon | None equals no coupon |
| TC-13 | EP | -1, -0.01, -1000 | ValueError | negative partition |
| TC-14 | EG | "abc", None, [], True | ValueError | wrong types (bool is not a number) |
| TC-15 | EG | NaN | ValueError | not-a-number |
| TC-16 | EP | 200, "welcome10" / "WELCOME20" / "" | ValueError | unknown or wrong-case coupon |
| TC-17 | EG | 10, "FAKE" | ValueError | invalid coupon rejected even when it would be ignored |
| TC-18 | BVA | 100.10 | 95.10 | half-up rounding (95.095) |
| TC-19 | EP | 250.0 (float) | 237.50 | float input accepted |
| TC-20 | EP | Decimal("500.00") | 450.00 | Decimal input accepted |
