from matplotlib import pyplot as plt
from math import floor 

delta_pop = 700_700 - 669_200
current_pop = 67_330_000 # 67.33 million (2021)

years = 100

next_n_years = [current_pop + delta_pop*i for i in range(years)]
print(next_n_years)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes

ax.plot(range(years),next_n_years)

ax.axvline(0,color="black")
ax.axhline(70_000_000,color="red")

# 70,000,000 = delta_pop*x + current_pop
# (70,000,000 - current_pop) / delta_pop = x

intersect = (70_000_000 - current_pop) / delta_pop
print("intersect", intersect)

ax.axvline(intersect,color="m")
ax.set_xticklabels([0,2021,2041,2061,2081,2101,2121])

year_intersect = 2021+intersect
percent_of_year = (year_intersect % 1)
days = percent_of_year * 365
print(year_intersect)
approx_month = days % 30
print("70,000,000 will be reach in the %.0fth month of %.0f." % (approx_month, floor(year_intersect)))

plt.show()