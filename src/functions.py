
def hello(str1, str2):
    print(str1, str2)

def hola():
    print("hola")

def add_numbers(num1, num2):
    print(num1 + num2)

def sum_v2(num1, num2):
    return num1 + num2

hello("hello","world")
add_numbers(1,2)
add_numbers(20, 60)
hola()


num1 = int(input("enter first number: "))


num3 = sum_v2(num1, num1)
print(num3)
