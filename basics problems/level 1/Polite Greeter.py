'''
### Problem 61 — Polite Greeter

**Scenario:** Write a function that greets a user by name.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.
'''

def greet(name):
    if not isinstance(name,str):
        raise TypeError('enter a string , only string !')
    
    print(f"hello {name} , haven't see you a while")

greet('fisal')