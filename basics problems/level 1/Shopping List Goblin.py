'''### Problem 26 — Shopping List Goblin

**Scenario:** Store grocery items in a list, then add, remove, and print them.

**What to do:**
- Solve it cleanly.
- Add at least 3 test cases.
- Think about one edge case.

**Focus:** lists'''

# adding an item
grocery = ['apples','milk','bread','watermelon']

def add_list(lst,item):

    lst += [item]
    print(lst)

add_list(grocery,'banana')


# removing an item 
def remove_list(lst,index):
    new_lst = []

    for i in range(len(lst)):
        if i != index:
            new_lst.append(lst[i])
    print(new_lst)

remove_list(grocery,0)