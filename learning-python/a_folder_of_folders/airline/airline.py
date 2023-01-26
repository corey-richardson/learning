import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

# Set up subplot grid
COLUMNS = 2
ROWS = 6
# Guide #
# 01 02 #
# 03 04 #
# 05 06 #
# 07 08 #
# 09 10 #
# 11 12 #
# n = and
plt.figure(figsize=(COLUMNS*6,ROWS*4))
ax1 = plt.subplot2grid((ROWS, COLUMNS), (0, 0))
ax2 = plt.subplot2grid((ROWS, COLUMNS), (0, 1))
ax3n4 = plt.subplot2grid((ROWS, COLUMNS), (1, 0), colspan=2)
ax5 = plt.subplot2grid((ROWS, COLUMNS), (2, 0))
ax6 = plt.subplot2grid((ROWS, COLUMNS), (2, 1))
ax7 = plt.subplot2grid((ROWS, COLUMNS), (3, 0))
ax8 = plt.subplot2grid((ROWS, COLUMNS), (3, 1))
ax9n11 = plt.subplot2grid((ROWS, COLUMNS), (4, 0), rowspan = 2)
ax10n12 = plt.subplot2grid((ROWS, COLUMNS), (4, 1), rowspan = 2)
plt.subplots_adjust(hspace=0.5)
plt.suptitle("How airline ticket prices vary:")

# Histogram w/ kde showing distribution of coach ticket price
ax1.set_title("Distribution of Coach Ticket Prices (Mean)")
ax1.set_xlabel("Price of a Coach Ticket")
sns.histplot(data=flight,x="coach_price",ax=ax1,kde=True)
# Red dashed vertical line at the mean price
mean_coach_price = flight.coach_price.mean()
ax1.axvline(mean_coach_price,color="red",linestyle="--")

##############


# Histogram w/ kde
ax2.set_title("Distribution of Coach Ticket Prices, t = 8 hours (Quartiles)")
ax2.set_xlabel("Price of a Coach Ticket where flight is 8 Hours")
sns.histplot(flight.coach_price[flight.hours == 8],ax=ax2,kde=True)
# sets red dashed vertical lines at each of the quartiles
# this shows the spread of the middle 50% of values
lqr = flight.coach_price[flight.hours == 8].quantile(0.25)
ax2.axvline(lqr,color="red",linestyle="--")
med = flight.coach_price[flight.hours == 8].median()
ax2.axvline(med,color="red",linestyle="--")
uqr = flight.coach_price[flight.hours == 8].quantile(0.75)
ax2.axvline(uqr,color="red",linestyle="--")

##################

# boxplot showing spread of flight delays
# trimmed to remove major outliers (in the thousands)
ax3n4.set_title("Boxplot distribution of flight delays (trimmed)")
ax3n4.set_xlabel("Delay")
sns.boxplot(x=flight.delay[flight.delay < 60], data=flight,ax=ax3n4)

#################

# scatterplots on the same axis showing clusters of coach prices and first class prices
sns.scatterplot(data=flight,x=flight.coach_price,y=flight.miles,ax=ax5)
sns.scatterplot(data=flight,x=flight.firstclass_price,y=flight.miles,color="orange",ax=ax5)
ax5.set_xlabel("Price")
ax5.set_ylabel("Distance (miles)")
ax5.set_title("Coach Prices vs First Class Prices")

#################

# histograms w/ kde lines comparing coach ticket prices for flights with and without:
# meal, entertainment or wifi

sns.histplot(data=flight,x="coach_price",hue="inflight_meal",kde=True,ax=ax6)
ax6.set_xlabel("Price")
ax6.set_title("Coach Prices Compared: In Flight Meal")

sns.histplot(data=flight,x="coach_price",hue="inflight_entertainment",kde=True,ax=ax7)
ax7.set_xlabel("Price")
ax7.set_title("Coach Prices Compared: In Flight Entertainment")

sns.histplot(data=flight,x="coach_price",hue="inflight_wifi",kde=True,ax=ax8)
ax8.set_xlabel("Price")
ax8.set_title("Coach Prices Compared: In Flight Wifi")

###############

# boxplots comparing ticket prices when:
# weekend or redeye flight
sns.boxplot(data=flight, x='coach_price', y="weekend",ax=ax9n11)
ax9n11.set_xlabel("Coach Price")
ax9n11.set_ylabel("Is weekend?")
sns.boxplot(data=flight, x='coach_price', y="redeye",ax=ax10n12)
ax10n12.set_xlabel("Coach Price")
ax10n12.set_ylabel("Is redeye?")

plt.savefig("plots.png",dpi=300)
plt.show()




