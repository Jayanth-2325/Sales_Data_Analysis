import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Salesup.csv")
quantity_sales=df.groupby('Month')['Quantity'].sum()
quantity_sales.plot(kind='bar')
plt.title("Monthly Quantity Sales")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.show()