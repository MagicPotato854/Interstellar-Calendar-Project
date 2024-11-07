import json
import sys
from convert_times import Planet
import time
from skyfield.api import load
from skyfield.api import Topos

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
    planets = load('de421.bsp')
    ts = load.timescale()
    t = ts.utc(2018, 11, 28, 0, 0, 0)
    earth = planets['earth'].at(t)
    atlanta_p = (planets['earth'] + Topos('33.7490 N', '84.3880 W'))
    atlanta = atlanta_p.at(t)

    print('TAI = %r' % (t.tai - 2400000.5))
    print('TT  = %r' % (t.tt  - 2400000.5))
    print('UT1 = %r' % (t.ut1 - 2400000.5))

    def dump_pv(p):
        print(' {{%.12f, %.12f, %.12f},\n'
            '  {%.12f, %.12f, %.12f}},' %
            (p.position.au[0], p.position.au[1], p.position.au[2],
            p.velocity.au_per_d[0], p.velocity.au_per_d[1], p.velocity.au_per_d[2]))

    def dump_altazd(p):
        print(' {%.12f, %.12f, %.12f},' %
            (p[0].degrees, p[1].degrees, p[2].au))

if sys.argv[1] == 'calculate':
    calculate()

sys.stdout.flush()