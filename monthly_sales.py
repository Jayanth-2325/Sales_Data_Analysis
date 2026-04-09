import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesup.csv")


monthly_sales = df.groupby('Month')['Total'].sum()
plt.figure()
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.show()