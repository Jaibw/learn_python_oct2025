## print table

number = int(input("Enter a number: "))

for i in range(1,11):
    print(i*number)

for i in range(number,number*10+1,number):
    print(i)

for i in range(number*10,1,-number):
    print(i)
