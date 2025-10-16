
list01 = [1, 2, 3]

list02 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

list03 = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

for item in list01:
    print(item)

for item in list02:
    for element in item:
        print(element, end=' ')
    print()

for item in list03:
    print(item)
