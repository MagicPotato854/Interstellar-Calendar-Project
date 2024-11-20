from astroquery.jplhorizons import Horizons
import time
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
def distcalc(planet1, planet2, units='au'):
    """
    Accepts two planet objects from the Horizons API and calculates the distance
    between them in the given units.
    """
    planet1_data = planet1.vectors()
    planet2_data = planet2.vectors()

    dist = ((planet1_data['x'] - planet2_data['x'])**2 + (planet1_data['y'] - planet2_data['y'])**2 + (planet1_data['z'] - planet2_data['z'])**2) ** 0.5
    if units.lower() == 'au':
        return round(float(dist), 5)
    if units.lower() == 'l': 
        lm = dist * 8.31675 
        lh = int(lm // 60) 
        lm -= lh * 60 
        ls = (lm % 1) * 60 
        lm = int(lm) 
        ls = round(float(ls))
        that_time = [lh, lm, ls] 
        return ':'.join([str(unit).zfill(2) for unit in that_time]) 
    return None
@app.route("/dist", methods=["GET"])
def distcalc2():
    date = request.args.get('date', time.time())
    p1 = request.args.get('p1', "earth")
    p2 = request.args.get('p2', "sun")
    units = request.args.get('units', "l")
    if date:
        date = (float(date) / 86400.0) + 2440587.5
    planets = {
        "sol": 10,
        "sun": 10,
        "mercury": 199,
        "venus": 299,
        "earth": 399,
        "mars": 499,
        "jupiter": 599,
        "saturn": 699,
        "uranus": 799,
        "neptune": 899,
        "pluto": 999,  # 134340
        "moon": 301,
        "luna": 301,
        "europa": 502,
        "titan": 606,
        "makemake": 136472,
    }
    planet1 = Horizons(id=planets[p1.lower()], location='500', epochs=date)
    planet2 = Horizons(id=planets[p2.lower()], location='500', epochs=date)
    return jsonify({
                    'distance': distcalc(planet1, planet2, units),
                    'p1': p1,
                    'p2': p2,
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
