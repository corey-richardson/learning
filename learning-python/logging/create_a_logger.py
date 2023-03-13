# The first step to utilizing the logging module is to import it into our 
# application. 
# We can do this using the following line of code:
import logging

# Next, we can obtain our logger object using the getLogger(name) method.
# This method takes in an optional, single input parameter called name that
# represents the name of the logger.
# We recommend using the built-in Python variable __name__ for this value 
# since it will return the current module’s name.
# This reduces the chance of accidentally reusing a logger name and 
# retrieving the wrong logger object.
logger = logging.getLogger(__name__)

# Next, we need to inform the logger where we want our logged messages to go. 
# To do this, we will use something called a handler.
# For Python, we will use the logging module’s StreamHandler class. 
# This class handles where our logged messages will output.
# Since we want our output to be direct to the console, we should supply 
# sys.stdout as the stream value. 
# Note that we must import the sys library to reference stdout as the stream 
# value.
import sys
stream_handler = logging.StreamHandler(sys.stdout)

# Finally, we can now add our stream handler object to the logger. 
# The logging module provides a method called addHandler(hdlr) that adds a 
# specific handler to the logger object.
logger.addHandler(stream_handler)