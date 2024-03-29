import pandas as pd
df = pd.read_csv("c:/users/s_baruah/desktop/data-3.csv")
df.head()

from matplotlib import pyplot as plt
plt.scatter(df['var1'], df['var2'])
plt.show()

df[1] = ((df['var1'] - (90.2))**2) + ((df['var2'] - (128.7))**2)
df[2] = ((df['var1'] - (130.5))**2) + ((df['var2'] - (156.8))**2)
df[3] = ((df['var1'] - (186.7))**2) + ((df['var2'] - (185))**2)

df['class'] = df[[1, 2, 3]].idxmin(axis=1)
print(df.head(30))

plt.scatter(df['var1'], df['var2'], c=df['class'])
plt.show()