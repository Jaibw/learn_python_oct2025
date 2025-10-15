myfile = open('demo.txt', 'r')

for line in myfile:
    print(line, end='')

myfile.close()
