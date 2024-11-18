import json
import sys
from convert_times import Planet
import time
from skyfield.api import load

def calculate():
    json_obj = open(sys.argv[2])
    data = json.load(json_obj)
    
    X = data["X"]
    y = data["y"]
    current_time = data["current_time"]
    planet_name = data["planet_name"]
    # do some your calculations based on X and y and put the result to the calculatedResults
    # print(make_pipeline)
    X *= 2
    y *= 3
    Earth = Planet("Earth", 8765.813, 24)
    Mars = Planet("Mars", 16487.52, 24.6599)
    Saturn = Planet("Saturn", 258240.845, 10.55)
    planet_list = [Earth, Mars, Saturn]
    calc_planet = None
    for i in planet_list:
        if i.name == planet_name:
            calc_planet = i
            break
    test_time = 17739855.401
    # current_time = time.time() / 3600 + 17259888
    calculatedResults = [calc_planet.print_time(current_time), time.asctime()] # it is just example of data to return, in fact you will calculate it below
    json_object_result = json.dumps(calculatedResults, indent=4)

    with open(sys.argv[3], "w") as outfile:
        outfile.write(json_object_result)
    print("OK")

def sky_field():
    # Load ephemeris data
    planets = load('de421.bsp')
    earth = planets['earth']
    mars = planets['mars']
    saturn = planets[6]  # Saturn is the 6th planet

    # Load timescale and get the current time
    ts = load.timescale()
    t = ts.now()

    # Calculate the distance between Earth and Mars
    earth_to_mars = earth.at(t).observe(mars).apparent().distance()
    distance_km = earth_to_mars.km  # Distance in kilometers
    distance_au = earth_to_mars.au  # Distance in astronomical units

    print(time.asctime())
    print(f"Distance between Earth and Mars:")
    print(f"{distance_km:.2f} km")
    print(f"{distance_au:.6f} AU")
    print(f"{(distance_au * 8.31675):.6f} light minutes")

try:
    if sys.argv[1] == 'calculate':
        calculate()
except IndexError:
    if __name__ == '__main__':
        sky_field()

sys.stdout.flush()