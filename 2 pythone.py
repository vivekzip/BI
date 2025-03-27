import pandas as pd

# Loading data into a DataFrame
data_frame = pd.read_csv('customers.csv')

# Displaying first five rows
print(data_frame.head())  

# Displaying last five rows
print(data_frame.tail())  

# Display column names
print(list(data_frame.columns))

# Display DataFrame info
data_frame.info()

# Display statistical summary
print(data_frame.describe())

# Removing missing values (if any)
data_frame = data_frame.dropna()

# Dropping the row at index 4 (5th row) and displaying first few rows
print(data_frame.drop(4).head())

# Renaming columns (Incorrect syntax in original code - needs `inplace=True` or assignment)
data_frame.rename(columns={0: "First", 1: "Second"}, inplace=True)

# Adding a new column with a constant value
data_frame['NewColumn'] = 1
print(data_frame.head())

# Sorting values by Age in descending order
print(data_frame.sort_values(by='Age', ascending=False).head())

# Sorting values by Age and Annual Income (k$)
print(data_frame.sort_values(by=['Age', 'Annual Income (k$)']).head(10))

# Creating first DataFrame
df1 = pd.DataFrame({
    'Name': ['Jeevan', 'Raavan', 'Geeta', 'Bheem'],
    'Age': [25, 24, 52, 40],
    'Qualification': ['MSc', 'MA', 'MCA', 'PhD']
})
print(df1)

# Creating second DataFrame
df2 = pd.DataFrame({
    'Name': ['Jeevan', 'Raavan', 'Geeta', 'Bheem'],
    'Salary': [100000, 50000, 20000, 40000]
})
print(df2)

# Merging two DataFrames
df = pd.merge(df1, df2, on="Name")  # Ensure merge is done on a common column
print(df)

# Function to classify customer satisfaction based on spending score
def fun(value):
    if value > 70:
        return "Yes"
    else:
        return "No"

# Applying the function to create a new column
data_frame['Customer Satisfaction'] = data_frame['Spending Score (1-100)'].apply(fun)

# Display first 10 rows with the new column
print(data_frame.head(10))
const = data_frame['Age'].max()
data_frame['Age'] = data_frame['Age'].apply(lambda x: x/const)
data_frame.head()
data_frame.plot(x ='CustomerID', y='Spending Score (1-100)',kind = 'scatter')

