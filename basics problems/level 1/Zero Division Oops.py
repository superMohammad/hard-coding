'''
### Problem 181 — Zero Division Oops

**Scenario:** Catch division by zero and print a helpful message.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.

**Focus:** try/except

'''

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("you can't devide on a zero , i got you !!")
    
print(div(2,1))