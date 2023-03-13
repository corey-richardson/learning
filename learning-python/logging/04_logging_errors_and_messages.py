# The logging module has several methods that we can use to log messages and
# errors with an assigned severity level.
# Those methods are:
# - debug(msg) which logs a message with level DEBUG
# - info(msg) which logs a message with level INFO
# - warning(msg) which logs a message with level WARNING
# - error(msg) which logs a message with level ERROR
# - critical(msg) which logs a message with level CRITICAL

# logger.debug("This is a debug message!")

# The logging module also provides a method log(level, msg) that allows us to 
# log a specific log level and message.

# logger.log(logging.INFO, "This is an info message!")

import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
        
def division():
  try:
    # Locate each input statement within the code. After each of these 
    # statements, add INFO log messages that show what value was entered.
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except ValueError:
    # Use the log(level, msg) method to log a CRITICAL message inside the 
    # division function except block. The log message should read No dividend
    # or divisor value entered!.
    logger.critical("No dividend or divisor value entered!")
    return None
  if divisor == 0:
    # Inside the division function, add an ERROR log message if dividing by 0.
    # The message should read: Attempting to divide by 0!.
    logger.error("Attempting to divide by 0!")
    return None
  else:
    return dividend/divisor
result = division()
# Add an if statement check to see if result is equal to None at the bottom of 
# script.py. If so, log a WARNING with the following message: 
# The result value is None!.
if result == None:
  logger.warning("The result value is None!")

# 1.
# Inside the terminal output, type python3 script.py and press Enter. 
# Type the following inputs, when prompted:
# Dividend = 6
# Divisor = 0

# 2.
# Inside the terminal output, execute python3 script.py with the 
# following inputs:
# Dividend = 6
# Divisor = blank (no value entered)

# 3.
# Inside the terminal output, execute python3 script.py with the 
# following inputs:
# Dividend = 6
# Divisor = 0

# 4.
# Inside the terminal output, execute python3 script.py with the 
# following inputs:
# Dividend = 6
# Divisor = 3

# OUT:
# $ python3 script.py
# Enter the dividend: 6
# Enter the divisor: 0
# Attempting to divide by 0!
# $ python3 script.py
# Enter the dividend: 6       
# Enter the divisor: 
# No dividend or divisor value entered!
# $ python3 script.py
# Enter the dividend: 6
# Enter the divisor: 0
# Attempting to divide by 0!
# The result value is None!
# $ python3 script.py
# Enter the dividend: 6
# Enter the divisor: 3
# $ 

# We will see that no DEBUG or INFO log messages show in our console. 
# Continue to the next exercise to learn why.