import pandas as pd
import matplotlib.pyplot as plt

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

## filter data
header("Print only pclass and name")
col_names = ['Pclass', 'Name']
print(df[col_names])
header("Print only pclass and name - 5")
print(df[col_names].head())
header("Print only pclass and name 20")
print(df[col_names].head(20))

header("Print only pclass and name where Age > 70")
col_names = ['Pclass', 'Name', 'Age']
print(df[df['Age'] > 70][col_names])

## handle missing data
header("Find null values")
print(df.isnull().sum())
header("Age Data")
print("Age Min: ",df["Age"].min())
print("Age Max: ",df["Age"].max())
print("Age Median: ",df["Age"].median())
df['Age'] = df['Age'].fillna(df['Age'].median())
header("Find null values")
print(df.isnull().sum())


## basic analysis
header("Survival by Gender")
#print(df.groupby('Sex')['Survived'].mean())
print(df.groupby('Sex')['Survived'].count())
header("Survival by Pclass - Passenger Class")
print(df.groupby('Pclass')['Survived'].count())
header("Survival by Pclass and Gender")
print(df.groupby(['Pclass','Sex'])['Survived'].count())

# Visualization
df.groupby('Pclass')['Survived'].count().plot(kind='bar', color='skyblue')
plt.title('Survival by Pclass and Gender')
plt.show()
