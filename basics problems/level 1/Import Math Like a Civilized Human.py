'''
### Problem 136 — Import Math Like a Civilized Human

**Scenario:** Use `math` to calculate square roots and pi-based formulas.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.

**Focus:** basic import

'''

import math 

def PI(num):
    return math.pi * num

def square(num):
    return math.sqrt(num)

print([PI(10),square(10)])