# When programming or debugging, we may want to focus on certain types of events. 
# Lucky for us, there are defined logging levels that indicate specific levels 
# of severity for a log message. 
# Each logging level is a constant within the logging module with an 
# associated numeric value. 
# The higher this numeric value, the higher the severity of the log message. 
# Each logging level is defined as:

# Level	Value
# NOTSET  	0
# DEBUG	   10
# INFO	   20
# WARNING	 30
# ERROR	   40
# CRITICAL 50

# We should use logging.DEBUG to provide detailed information that is useful 
# for debugging the application. 
# It has a numeric value of 10.

# We should use logging.INFO for general operations where expected information 
# or output is logged.
# It has a numeric value of 20.

# We should use logging.WARNING to alert us to a current or impending, 
# unexpected issue or error.
# This logging level does mean that the software or application will continue 
# to run despite the warning message.
# It has a numeric value of 30.

# We should uselogging.ERROR to indicate serious problems that cause 
# functionality within the software or application to break.
# It has a numeric value of 40.

# We should use logging.CRITICALfor the most severe of errors and issues. 
# These errors indicate that the software or application may stop running 
# altogether.
# It has a numeric value of 50.

# Finally, the logging.NOTSET logging level searches for the first non-NOTSET
# ancestor logger and inherits its logging level.
# If there is none, our output threshold will be zero.

#################################################

# Print the numeric values of each logging level. 
# Remember to import the logging module. 
# Later in this lesson, we will show how we can use these levels to control
# which logging messages get outputted.

import logging
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)
print(logging.NOTSET)