"""
Enter a number: 5

*
* *
* * *
* * * *
* * * * *
"""
num1 = int(input("Enter a number: "))


for i in range(1,num1+1):
    print("* "*i)
