'''
### Problem 106 — Class Attendance

**Scenario:** Use a list to store present students and print absentees from a master list.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.

'''

class_students = ['mohammad','ahmad','khaled','yasser','faisal','ayman']

def abs_and_pres(lst,*args):
    all_students = class_students.copy()
    present = []
    absents = []

    for student in args:
        if student in all_students:
            present.append(student)
        else:
            print(f"{[student]} not registered to the class")

    for student in all_students:
        if student not in present:
            absents.append(student)

    return present , absents



print(abs_and_pres(class_students,'mohammad','ahmad'))