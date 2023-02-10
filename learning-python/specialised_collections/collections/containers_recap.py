# First, create a variable called company_name which contains a string representing our clothing company’s name. Come up with something *creative*
company_name = "The Clothing Brand"

# Next, create a tuple called company_location which contains two decimal values for latitude and longitude. Feel free to use any coordinates.
# Latitude: 51.5085 Longitude: -0.1257.
company_location = (51.5085, -0.1257)

#Create a list of strings called company_products representing which products we will be selling in our store. Make sure there are at least 5 products.
company_products = [f"Product No. {i+1}" for i in range(5)]

# Finally, create a dictionary that will store all of the previous values we created into a variable called company_data.
# Use the keys name, location, and products with the values being the respective variables we created in the last steps.
company_data = {"name": company_name, "location": company_location, "products": company_products}

print(company_data)