import datetime    ## https://docs.python.org/3/library/datetime.html#datetime.datetime.today 

date = datetime.datetime.today()

name = "John"
print(f"Hello, {name} , Date: {date:%A, %d %B-%Y}")

