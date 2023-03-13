import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(message)s]')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

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
    logger.error("The TO country supplied is not a valid country.")
    sys.exit(0)
    
  if from_country not in exchange_rates:
    logger.error("ERROR: The FROM country supplied is not a valid country.")
    sys.exit(0)
        
  to_rate = exchange_rates[to_country]
  from_rate = exchange_rates[from_country]
    
  if from_country != "USD":
    converted_to_usd = amount / from_rate
    logger.info("Converting from {from_country} to USD: {converted_to_usd}".format(from_country=from_country, converted_to_usd=converted_to_usd))
        
    converted_from_usd = converted_to_usd * to_rate
    logger.info("Converting from USD to {to_country}: {converted_from_usd}".format(to_country=to_country, converted_from_usd=converted_from_usd))
        
    return converted_from_usd
        
  else:
    converted_from_usd = amount * to_rate
    logger.info("Converting from USD to {to_country}: {converted_from_usd}".format(to_country=to_country, converted_from_usd=converted_from_usd))
    return converted_from_usd
        
logger.debug("Current rates: {exchange_rates}".format(exchange_rates=exchange_rates))        
currency = convert("EUR", "USD", 45)
print(currency)