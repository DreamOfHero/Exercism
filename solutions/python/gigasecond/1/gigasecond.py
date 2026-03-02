import datetime

# Define the constant for one billion seconds (10^9)
# Using underscores makes the number easier to read at a glance
GIGA_SECOND = 1_000_000_000

def add(moment):
    # Create a timedelta object representing the duration of one gigasecond
    time_delta = datetime.timedelta(seconds=GIGA_SECOND)
    
    # Add the duration to the initial datetime object (moment)
    # Python's datetime module handles all the complex calendar logic automatically
    result = moment + time_delta
    
    return result
