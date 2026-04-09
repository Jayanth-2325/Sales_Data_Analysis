import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Salesup.csv")
gender_sales=df.groupby('Gender')['Total'].sum()
gender_sales.plot(kind='pie',autopct='%1.1f%%')
plt.title("Gender sales")
plt.ylabel("")
plt.show()