string01 = input("Enter a string: ")

print(string01)
print("Length of string01:", len(string01))
print("First character of string01:", string01[0])
print("Last character of string01:", string01[-1])

string01 = string01.replace("hello", "hola")
print(string01)

string02 = "Hello"
string03 = "World!"
print(string02, string03)
print(string02 + string03)

amount = 10.00
print("Amount: %f" % amount)
print("Amount: %.2f" % amount)
