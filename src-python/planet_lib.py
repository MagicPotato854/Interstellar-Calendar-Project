from math import floor

def hours_to_earth(hours):
    """
    Take the number of hours since Jan 1, year 1 at 12:00 AM and return the current time.
    returns:
    (year, day of the year, hours into day, minutes into hour, seconds into minute)
    """

    # Declare and define variables
    years = 0
    days = 0
    minutes = 0
    seconds = 0
    leftovers = hours % 1

    # Get the number of years
    while hours >= 8760:
        year = years + 1
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            hours -= 8784
            years += 1
        else:
            hours -= 8760
            years += 1

    # Get the number of days
    while hours >= 24:
        hours -= 24
        days += 1

    # Get the number of hours
    hours = floor(hours)

    # Get the number of minutes
    minutes = floor(60 * leftovers)
    leftovers -= minutes / 60

    # Get the number of seconds
    seconds = 3600 * leftovers

    return years + 1, days, hours, minutes, seconds