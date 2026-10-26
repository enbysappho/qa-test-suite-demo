# Test plan: order total calculation

## 1. Scope
In scope: `src/pricing.py` (`final_total`): volume discount, coupon rule, input validation, rounding.
Out of scope: payment, tax, shipping, UI.

## 2. Test approach
- Black-box functional tests derived from the written specification (docstring in `src/pricing.py`).
- Techniques: equivalence partitioning, boundary value analysis, error guessing (see `TEST_CASES.md`).
- Level: unit tests with Python `unittest`. Every test case has an ID (TC-xx) used in the test names.

## 3. Entry and exit criteria
- Entry: specification reviewed, code builds.
- Exit: all 20 test cases pass and every boundary in the specification (0, 50, 100, 500) is covered.

## 4. Risks
| Risk | Mitigation |
|---|---|
| Floating-point rounding errors | Money handled with `Decimal`; rounding tests TC-18 to TC-20 |
| Off-by-one at band edges | BVA at 99.99 / 100 and 499.99 / 500 |
| Ambiguous spec (coupon vs. volume discount order) | Behaviour written down in the spec and tested in TC-11 |

## 5. Defect handling
Report defects with `BUG_REPORT_TEMPLATE.md`: steps, expected vs. actual result, severity and priority.

## 6. How to run
```bash
python -m unittest discover -s tests -v
```
