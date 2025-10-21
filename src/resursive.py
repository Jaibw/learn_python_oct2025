"""
Enter a number: 5

5
4
3
2
1
"""
def print_num(num):
    i = num
    while i > 0:
        print(i)
        i = i - 1

def print_num2(num):
    if num > 0:
        print(num)
        print_num2(num-1)


num01 = int(input("Enter a number: "))
print_num2(num01)


