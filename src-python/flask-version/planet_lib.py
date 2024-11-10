from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
from math import floor

app = Flask(__name__)
CORS(app)

# Offset in hours from "year 1, January 1" to "1970, January 1" is about 17,327,424 hours
HOURS_OFFSET = 17_327_424

def hours_to_earth(hours):
    """Convert hours since 'year 1' to an Earth datetime using datetime."""
    base_date = datetime(year=1, month=1, day=1)  # Start from year 1
    delta = timedelta(hours=hours)  # Use the exact hours directly without extra offset subtraction
    return base_date + delta

def print_earth_time(date):
    """Formats the datetime for readable output."""
    return date.strftime("%a %b %d %H:%M:%S %Y")

def hours_to_mars(hours):
    """
    Converts Earth hours to Martian date based on an accurate Martian calendar.
    A Martian year alternates between 668 and 669 days:
    - Leap years occur every odd year and every year divisible by 10, except those divisible by 100.
    """
    # Martian day and year lengths
    hours_per_martian_day = 24.6599
    normal_martian_year_hours = 668 * hours_per_martian_day
    leap_martian_year_hours = 669 * hours_per_martian_day

    year = 0

    # Calculate Martian years by subtracting each year's hours until the remaining hours fit within a year
    while hours >= (leap_martian_year_hours if (year % 2 != 0 or year % 10 == 0) and year % 100 != 0 else normal_martian_year_hours):
        if (year % 2 != 0 or year % 10 == 0) and year % 100 != 0:
            hours -= leap_martian_year_hours
        else:
            hours -= normal_martian_year_hours
        year += 1

    # Calculate the remaining Martian days and time in hours, minutes, and seconds
    day = int(hours // hours_per_martian_day)
    remaining_hours = hours % hours_per_martian_day
    minutes = int((remaining_hours % 1) * 60)
    seconds = round((remaining_hours * 3600) % 60, 3)

    return year + 1, day + 1, int(remaining_hours), minutes, seconds

def format_planet_time(date, day_len=0):
    """Formats a Martian date into a readable string based on provided day length."""
    if day_len < 100:
        return f"Year {date[0]}, day {date[1]}, " + "{:02}:{:02}:{:02}".format(date[2], date[3], floor(date[4]))
    elif day_len >= 1000:
        return f"Year {date[0]}, day {date[1]}, " + "{:04}:{:02}:{:02}".format(date[2], date[3], floor(date[4]))
    else:
        return f"Year {date[0]}, day {date[1]}, " + "{:03}:{:02}:{:02}".format(date[2], date[3], floor(date[4]))

@app.route("/earth_time", methods=["GET"])
def earth_time():
    hours = float(request.args.get("hours", 0))
    date = hours_to_earth(hours)
    formatted_time = print_earth_time(date)
    return jsonify({"earth_time": formatted_time})

@app.route("/mars_time", methods=["GET"])
def mars_time():
    hours = float(request.args.get("hours", 0))
    mars_date = hours_to_mars(hours)
    formatted_time = format_planet_time(mars_date, 11)  # Assuming a day length of 11 for format
    return jsonify({
        "mars_year": mars_date[0],
        "mars_day": mars_date[1],
        "hours": mars_date[2],
        "minutes": mars_date[3],
        "seconds": mars_date[4],
        "formatted_time": formatted_time
    })

# This block only runs if the script is executed directly
if __name__ == "__main__":
    # Test calculations (these will only run once when you start the server)
    spectime = 17739736.883
    date = hours_to_earth(spectime)
    print(print_earth_time(date))
    print(hours_to_mars(spectime))
    print(format_planet_time(hours_to_mars(spectime), 11))
    
    # Start the Flask server
    app.run(debug=True)
