import time

hours_to_earth = lambda hours: time.gmtime((hours - 17_259_912) * 3600)
print_earth_time = lambda date: print(time.ctime(date)) \
    if type(date) == float or type(date) == int else print(time.asctime(date))

date = hours_to_earth(17739736.883)
print_earth_time(date)