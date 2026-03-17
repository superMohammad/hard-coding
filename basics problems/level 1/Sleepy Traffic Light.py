'''### Problem 1 — Sleepy Traffic Light

**Scenario:** Write a program that prints `stop`, `ready`, or `go` based on a light color input. Handle unknown colors too.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.

**Focus:** if / elif / else'''

def traffic(color):
    if not isinstance(color,str):
        raise TypeError('enter a string please')
    
    color = color.lower()

    if color == 'green':
        print('go')
    elif color == 'orange':
        print('ready')
    elif color == 'red':
        print('stop!')
    else:
        print("i don't know the color meaning.")

traffic('RED')