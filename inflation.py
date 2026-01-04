import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Inflation": [0.6, -0.1, 1.9, 8.1, 5.7]
}

df = pd.DataFrame(data)

print(df)
df.plot(x="Year", y="Inflation", kind="line")
plt.show()
