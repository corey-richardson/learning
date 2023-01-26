# Data from
# https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who

import pandas as pd
df = pd.read_csv("Life Expectancy Data.csv")
#print(df.head())

import seaborn as sns
import statsmodels.api as sm
from matplotlib import pyplot as plt

# How does life expectancy correlate to other variables such as: 
# Adult Mortality, Infant Mortality, GDP

# sns.lmplot(data=df,x="Alcohol",y="GDP",hue="Status")
# plt.show()

# How does life expectancy depend on a countries presence of disease and vaccinations
m = sm.OLS.from_formula("Life_expectancy ~ Measles + Polio + Diphtheria",data=df).fit()
# print(m.params)

measles = int(input("Measles: "))
polio = int(input("Polio: "))
diphtheria = int(input("Diphtheria: "))

life_expectancy = m.params[0] \
    + m.params[1] * measles \
        + m.params[2] * polio \
            + m.params[3] * diphtheria
            
print("A country with %i case of measles per 1000 people,\
    \n%i%% immunisation coverage for polio amongst 1 year olds and,\
    \n%i%% immunisation coverage for diphtheria amongst 1 year olds,\
    \nshould have a life expectancy of %.1f." % (measles,polio,diphtheria,life_expectancy))

# Other factors can also influence the life expectancy and as such I don't expect
# this to be 100% accurate.
# Also there are datapoints saying 15,000 / 1000 people have polio which I believe
# would likely skew the data.
# To improve accuracy I could track more variables

# In: 492 58 62
# Exp: 59.9
# Act: 53.4
# Dif: 6.5

# In: 15374 87 87 --> not exactly sure how you can have 15,374 / 1000 but blame WHO
# Exp: 71.7
# Act: 53.4
# Dif: 18.3
# Note: understandable given the fact the data seems wonky

# In: 112 95 95
# Exp: 74.9
# Act: 72.2
# Dif: 2.7

