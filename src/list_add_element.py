"""
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

generate a list that will be result of vertical sum of elements
list_sum = [12, 15, 18]
"""
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

def add_item(a1, a2, a3):
    return a1 + a2 + a3

def add(list1, list2, list3):
    list_sum = []
    for x in range(0,3):
        total = add_item(list1[x] , list2[x] , list3[x])
        list_sum.append(total)
    return list_sum

list_sum = add(list1, list2, list3)
print(list_sum)
