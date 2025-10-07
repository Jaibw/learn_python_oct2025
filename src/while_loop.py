numbers = []

while True:
    i = int(input("Enter a number: "))
    numbers.append(i)
    if i == 0:
        break
print("Sum: ", sum(numbers))
