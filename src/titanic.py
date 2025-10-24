import pandas as pd
def header(message):
    print('=' * 100)
    print(message)
    print('=' * 100)

## load data
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
header("Print few records")
print(df.head(2))

## understand data
header("Print Basic Information")
df.info()
header("Shape of my data")
print(df.shape)
header("Column names")
print(df.columns)
header("statistics of my data")
print(df.describe())
