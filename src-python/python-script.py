import json
import sys
from convert_times import Planet
import time

def first_function():
    json_obj = open(sys.argv[2])
    data = json.load(json_obj)
    
    X = data["X"]
    y = data["y"]
    # do some your calculations based on X and y and put the result to the calculatedResults
    # print(make_pipeline)
    X *= 2
    y *= 3
    Earth = Planet("Earth", 8765.813, 24)
    Mars = Planet("Mars", 16487.52, 24.6599)
    Saturn = Planet("Saturn", 258240.845, 10.55)
    test_time = 17739855.401
    current_time = time.time() / 3600 + 17259888
    calculatedResults = [Mars.print_time(current_time), time.asctime()] # it is just example of data to return, in fact you will calculate it bellow
    json_object_result = json.dumps(calculatedResults, indent=4)

    with open(sys.argv[3], "w") as outfile:
        outfile.write(json_object_result)
    print("OK")


if sys.argv[1] == 'first_function':
    first_function()

sys.stdout.flush()