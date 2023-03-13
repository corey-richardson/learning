import logging
import sys

from datetime import datetime

exchange_rates = {
  "USD": 1.0,
  "EUR": 0.861775,
  "GBP": 0.726763,
  "INR": 75.054725,
  "AUD": 1.333679,
  "CAD": 1.237816,
  "SGD": 1.346851
}

def convert(from_country, to_country, amount):
  if to_country not in exchange_rates:
    timestamp = datetime.now()
    print(timestamp)
    print(__name__)
    print("ERROR: The TO country supplied is not a valid country.")
    sys.exit(0)
    
  if from_country not in exchange_rates:
    timestamp = datetime.now()
    print(timestamp)
    print(__name__)
    print("ERROR: The FROM country supplied is not a valid country.")
    sys.exit(0)
        
  to_rate = exchange_rates[to_country]
  from_rate = exchange_rates[from_country]
    
  if from_country != "USD":
    converted_to_usd = amount / from_rate
    timestamp = datetime.now()
    print(timestamp)
    print(__name__)
    print("INFO: Converting from {from_country} to USD: {converted_to_usd}".format(from_country=from_country, converted_to_usd=converted_to_usd))
        
    converted_from_usd = converted_to_usd * to_rate
    timestamp = datetime.now()
    print(timestamp)
    print(__name__)
    print("INFO: Converting from USD to {to_country}: {converted_from_usd}".format(to_country=to_country, converted_from_usd=converted_from_usd))
        
    return converted_from_usd
        
  else:
    converted_from_usd = amount * to_rate
    timestamp = datetime.now()
    print (timestamp)
    print (__name__)
    print ("INFO: Converting from USD to {to_country}: {converted_from_usd}".format(to_country=to_country, converted_from_usd=converted_from_usd))
    return converted_from_usd
        
timestamp = datetime.now()
print(timestamp)
print(__name__)
print("DEBUG: Current rates: {exchange_rates}".format(exchange_rates=exchange_rates))        
currency = convert("EUR", "USD", 45)
print(currency)
        
        
    