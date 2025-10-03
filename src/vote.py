username = input("Enter your name: ")
age = int(input("Enter your age: "))

if username == "":
    print("You didn't enter a name") 
    
if age >= 18:
    print("Congratulations! You are old enough.")
    print("You can vote!")
else:
    print("Sorry, you are not old enough.")
    print("You can not vote!")
