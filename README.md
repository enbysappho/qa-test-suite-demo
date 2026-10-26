# qa-test-suite-demo

A small **software testing** portfolio project: a documented test plan, test cases and an automated unit test suite
for an order-total function (volume discount + coupon + validation + rounding).

## What is inside
| Path | Content |
|---|---|
| `src/pricing.py` | System under test, with its specification in the docstring |
| `tests/test_pricing.py` | Automated tests (`unittest`), traceable to test case IDs |
| `docs/TEST_PLAN.md` | Scope, approach, entry/exit criteria, risks |
| `docs/TEST_CASES.md` | 20 test cases using equivalence partitioning, boundary value analysis, error guessing |
| `docs/BUG_REPORT_TEMPLATE.md` | Defect report format |

## Run
```bash
python -m unittest discover -s tests -v
```
No external packages needed.

## Skills shown
Test design techniques, traceability (test case IDs in code and docs), edge-case thinking (rounding, NaN, wrong types),
defect reporting.

> Built with AI assistance (Claude). I reviewed and run the code myself.
