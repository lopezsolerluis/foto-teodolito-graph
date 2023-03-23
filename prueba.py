import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('microbit.csv')

print(df)
df.plot()
plt.show()
