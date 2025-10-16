


list02 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

list03 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]


list_sum = []

for i in range(0,3):
    row = []
    for j in range(0,3):
        # print(list02[i][j], end=" + ")
        # print(list03[i][j], end=" :")
        # print(list02[i][j] + list03[i][j])
        row.append(list02[i][j] + list03[i][j])
    list_sum.append(row)
    # print("")

for item in list_sum:
    for element in item:
        print(element, end=' ')
    print()
