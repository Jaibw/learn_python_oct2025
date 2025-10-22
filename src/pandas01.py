import pandas as pd

students = {
    'Name' : ["Mark", "John", "Alexander" ],
    'Age' : [20, 26, 30],
    'City': ['New York', 'Toronto', 'Chicago']
}

df = pd.DataFrame(students)
print(df)
