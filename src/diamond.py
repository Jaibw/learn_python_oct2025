"""
 *
* *
 *
"""

num = 10

if num <= 1:
    print("*")
else:
    for i in range(1,num+1):
        for j in range(num,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print("")
    for i in range(num-1,0,-1):
        for j in range(num,i,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end=" ")
        print("")
