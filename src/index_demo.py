str1 = 'Hello World'
for x in range(len(str1)):
    print(str1[x], end='_')
    
print()
print('='*20)

for x in range(-1, (-1 * len(str1)) -1, -1):
    print(str1[x], end='_')
