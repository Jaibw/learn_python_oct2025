"""
and
or
not
"""

a1 = 21
b1 = -1

if not a1 == 20:    # alternative a1 != 20
    print('A1 is equal to 20')
else:
    print("A1 is 20")

if a1 > 0 and b1 > 0:
    print("A1 and B1, both are greater than 0")
else:
    print("One of them is less than 0")

if a1 > 0 or b1 > 0:
    print("One of then is greater than 0")

if not (a1 > 0 and b1 > 0):
    print("Just a experiment")
