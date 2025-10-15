def hello():
    print("Hello World!")

def message(str1):
    print(str1)

def add_num(num1, num2):
    return num1 + num2

def add_sub(num1, num2):
    total = num1 + num2
    sub = num1 - num2
    return total, sub

hello()
message("Hello World!")
print("Sum: ", add_num(1, 2))

sum1, sub  = add_sub(2, 2)
print(sum1, sub)
