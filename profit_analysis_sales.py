import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Salesup.csv")
profit=df.groupby('Product line')['gross income'].sum()
profit.plot(kind='bar')
plt.title('Profit analysis')
plt.show()