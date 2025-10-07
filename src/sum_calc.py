"""
Take the input(any) for the user, and then sum all the numbers

e.g.
Enter a number: 10
Enter a number: 5
Enter a number: 0

Sum: 15
"""
list1 = []

for num in range(100):
    i1 = int(input("Enter a number: "))
    list1.append(i1)
    if i1 == 0:
        break

print("Sum:",sum(list1))
