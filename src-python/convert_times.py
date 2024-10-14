from math import floor
from time import time
# from skyfield.api import load

"""
ts = load.timescale()
t = ts.now()
"""

class Planet:
    def __init__(self, name, len_year, len_day):
        self.name = name
        self.len_year = len_year
        self.len_day = len_day
        self.days_in_year = len_year / len_day

    def convert_in(self, hours):
        years = hours // self.len_year
        hours -= years * self.len_year
        days = hours // self.len_day
        hours -= days * self.len_day
        seconds = hours % 1 * 60 % 1 * 60
        return years, days, hours, seconds

    def convert_to_hours(self, local_time):
        return local_time[0] * self.len_year + local_time[1] * self.len_day + local_time[2]

    def convert_to_planet(self, time, planet):
        return  planet.convert_in(self.convert_to_hours(time))

    def print_time(self, hours):
        local_time = self.convert_in(hours)
        # print(f"{self.name}'s Date: Year {1 + floor(local_time[0])}, day {1 + floor(local_time[1])}, {floor(local_time[2])}:{floor(local_time[2] % 1 * 60)}")
        return f"{self.name}'s Date: Year {1 + floor(local_time[0])}, day {1 + floor(local_time[1])}, {floor(local_time[2])}:{floor(local_time[2] % 1 * 60)}:{floor(local_time[3])}"

"""
Earth = Planet("Earth", 8765.813, 24)
Mars = Planet("Mars", 16487.52, 24.6599)
Saturn = Planet("Saturn", 258240.845, 10.55)
test_time = 17739855.401
current_time = time() / 3600 + 17259888


Earth.print_time(current_time)
Mars.print_time(current_time)
Saturn.print_time(current_time)
"""