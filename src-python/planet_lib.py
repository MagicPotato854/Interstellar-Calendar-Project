import time
from math import floor

# These only work for the year after 1970
hours_to_earth = lambda hours: time.gmtime((hours - 17_259_912) * 3600)
print_earth_time = lambda date: print(time.ctime(date)) \
    if type(date) == float or type(date) == int else print(time.asctime(date))


def hours_to_mars(hours):
    """
    We are going to use a proposed Martian Calendar that is extremely accurate.
    A year changes between 668 and 669 days. A "Leap Year" occurs every odd
    year, every year divisable by ten but not divisable by 100.
    """
    year = 0
    while hours >= 16497.4731:
        year += 1
        if (year % 2 != 0 or year % 10 == 0) and year % 100 != 0:
            hours -= 16497.4731  # Normal year (Or leap year)
        else:
            hours -= 16472.8132  # Drop year

    day = hours // 24.6599
    hours -= day * 24.6599
    leftovers = hours % 1
    hours -= leftovers
    minutes = floor(leftovers * 60)
    leftovers -= minutes / 60
    seconds = leftovers * 3600

    return year + 1, int(day + 1), int(hours), minutes, round(seconds, 3)


def print_planet_time(date):
    """
    Prints a date in human readable format.
    date should be a tuple formatted like the following:
    (year, day, hours, minutes, seconds)
    """
    print(f"Year {date[0]}, day {date[1]}, " + "{:02}:{:02}:{:02}".format(date[2], date[3], floor(date[4])))


spectime = 17739736.883
date = hours_to_earth(spectime)
print_earth_time(date)
print(hours_to_mars(spectime))
print_planet_time(hours_to_mars(spectime))