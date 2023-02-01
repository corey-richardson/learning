# Immutable data types are important to use in functional programming as 
# they offer advantages, such as:
#   thread-safe data manipulation
#   preventing programmers from accidentally changing a value

# NAMED TUPLES

# from collections import namedtuple
 
# # create a class called student
# student = namedtuple("student", ["name", "age", "grade"]) 
 
# # Create tuples for the three students
# scott = student("Scott", 28, 'A')
# nicole = student("Nicole", 26, 'B')
# john = student("John", 29, 'D')
 
# # Access Scott’s information for example
# print(scott.name) # Output: Scott
# print(scott.age) # Output: 28
# print(scott.grade) # Output: ‘A’

# We can package three student tuples neatly into a tuple called students 
# like so:
# students = (scott, nicole, john)

# ---

# Checkpoint 1
# Create a namedtuple called country to represent a country. It should contain 
# fields to represent the name of a country, its capital, and the continent 
# on which it is located.
# The country tuple should contain name, capital, and continent as fields.

# Checkpoint 2
# Create three tuples that represent the following countries:
#   France: capital: Paris, continent: Europe
#   Japan: capital: Tokyo, continent: Asia
#   Senegal: capital: Dakar, continent: Africa

# Checkpoint 3
# Pack all three countries into a tuple named countries.

# ---

from collections import namedtuple

# Checkpoint 1
country = namedtuple("country", ["name", "capital", "continent"])
# Checkpoint 2
france = country("France","Paris","Europe")
japan = country("Japan","Tokyo","Asia")
senegal = country("Senegal","Dakar","Africa")
# Checkpoint 3
countries = (france, japan,senegal)