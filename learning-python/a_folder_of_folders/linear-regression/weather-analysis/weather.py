# Data source
# https://www.kaggle.com/datasets/budincsevity/szeged-weather?resource=download

# Imports:
# pandas, statsmodels.api, seaborn, matplotlib

import pandas as pd
df = pd.read_csv("weatherHistory.csv")

import statsmodels.api as sm
import seaborn as sns
from matplotlib import pyplot as plt

# corr_grid = df.corr()
# sns.heatmap(corr_grid)
# plt.show()

# How does humidity change with temperature?
# sns.lmplot(data=df, x="Temperature",y="Humidity",hue="Summary",fit_reg=False)
# plt.show()

model = sm.OLS.from_formula("Humidity ~ Temperature", data = df).fit()
print(model.params)

# If temp = 16 degrees:
accepted = False
while True:
    temp_in = input("Enter temperature: ")
    if temp_in == "break":
        break
    try:
        temp_in = float(temp_in)
        accepted = True
        break
    except ValueError:
        print("Please enter a number.")

if accepted == True:    
    temp = {"Temperature":temp_in}
    predicted_humidity = model.predict(temp)
    print("If temperature is %i degrees celsius, humidity will be ~%.2f%%" % (temp_in,predicted_humidity*100))
    
# input: 9.472222222222221
# expected output: 0.89
# actual output: 0.77
# difference: -0.12, -13%

# input: 17.800000000000004
# expected output: 0.55
# actual output: 0.66
# difference: +0.11, 20%

# input: 10.65
# expected output: 0.70
# actual output: 0.75
# difference: +0.05, 7%

# input: -4.183333333333334
# expected output: 0.92
# actual output: 0.94
# difference: +0.02, 2%

# note that these tests are taken from specific datapoints and could therefore be outliers
# average difference = +0.015, 4%