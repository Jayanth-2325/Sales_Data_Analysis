import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("salesup.csv")

category_sales = df.groupby('Product line')['Total'].sum()

category_sales.plot(kind='bar')
plt.title("Category-wise Sales")
plt.xticks(rotation=45)
plt.show()