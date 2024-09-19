import pandas as pd


d = {'UK': 0, 'USA': 1, 'N': 2}
df = pd.read_csv("data2.csv")
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

feat


print(df)
