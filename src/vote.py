username = input("Enter your name: ")
age = input("Enter your age: ")

if len(username) < 1:
    print("You didn't enter a name")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Congratulations! You are old enough.")
        print("You can vote!")
    else:
        print("Sorry, you are not old enough.")
        print("You can not vote!")
else:
    print("You didn't enter a correct value for age")
