import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [8.00, 4.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Item_Name", "Qty_sold"]
df = pd.read_csv("Sales.csv",usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.Item_Name, df.Qty_sold)
plt.show()
