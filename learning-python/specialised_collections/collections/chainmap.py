# The ChainMap container allows us to store many mappings in an ordered group,
# but lookups (accessing the value using a key) are repeated for every mapping
# inside of the ChainMap until something is found or the end is reached. 
# If we try to modify the data in any way, then only the first mapping in the 
# ChainMap will receive the changes.
# One way to think of the ChainMap is that it treats all of the stored
# dictionaries as one large dictionary, where if there are repeated keys, then
# the first found result is returned.

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# First, remember to import ChainMap.
from collections import ChainMap
# Then create a new ChainMap called profit_map using the year_profit_data list. 
# Remember that a ChainMap accepts a variable number of arguments so we need to
# expand the list (*) so the constructor will read them as individual arguments
# instead of one single argument.
profit_map = ChainMap(*year_profit_data)

# Create a function called get_profits which calculates the sum of the standard
# profits (keys not containing 'holiday') and the holiday profits (keys 
# containing 'holiday') in two different variables.
# Make this function return the two variables: the standard profit first and 
# the holiday profit second. 
# Additionally, call the function using the profit_map and store the results in
# variables called last_year_standard_profit and last_year_holiday_profit.
# When creating this function, you can loop through each of the keys in the 
# ChainMap since it is treated like one big dictionary.
# If 'holiday' is in the key, then add the value to the total count for the 
# holiday profit, otherwise add the value to the standard profit. 
# Remember to return both values.
def get_profits(c_map):
    total_standard_profit = 0
    total_holiday_profit = 0
    for key in c_map.keys():
        if "holiday" in key:
            total_holiday_profit += c_map[key]
        else:
            total_standard_profit += c_map[key]
    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

# It has been three months and our accountant has sent three more months worth
# of profit data in the form of a list of dictionaries called new_months_data.
# Add the new mappings to the profit_map so that the old January - March months
# are still in the ChainMap, but accessing those keys will return data for the
# most recent three months.
# Call the get_profits function on the profit_map again and store the results 
# in current_year_standard_profit and current_year_holiday_profit to calculate
# the sum of the most recent 12 months of profit data.
# Remember to add new dictionaries to the profit_map instead of updating the 
# first dictionary in the group of mappings. 
# To do this you can use .new_child(new_dictionary). 
# Keep in mind that this method returns a new ChainMap object, so you will need
# to replace the old version of profit_map.
for item in new_months_data:
    profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = \
    get_profits(profit_map)

# Calculate the difference for the standard and holiday profits and store them
# in variables called year_diff_standard_profit and year_diff_holiday_profit. 
# Print out the results to see the difference in profit for the current 12
# month period.
year_diff_standard_profit = \
    current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = \
    current_year_holiday_profit - last_year_holiday_profit

print(f"Standard: {year_diff_standard_profit}")
print(f"Holiday: {year_diff_holiday_profit}")
