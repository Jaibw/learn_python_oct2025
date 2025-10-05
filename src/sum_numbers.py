"""
## Create a program that will take five numbers and print the sum

Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
Enter number 4: 4
Enter number 5: 5

Sum: 15
"""

sum = 0
for i in range(1,6):
    num = int(input("Enter number {}: ".format(i)))
    sum = sum + num  # sum += num 

print("Sum: {}".format(sum))
