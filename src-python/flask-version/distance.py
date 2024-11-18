import time
import calendar
from astroquery.jplhorizons import Horizons


def getdist(date=None , p1='sol', p2='earth', units='au'):
    if date:
        date = (date / 86400.0) + 2440587.5
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
    print(f"The communication time between {p1.title()} and {p2.title()} is {distcalc(planet1, planet2, units)}")


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


if __name__ == '__main__':
    # getdist(calendar.timegm(time.strptime('2000 01 01 00 00 00', '%Y %m %d %H %M %S')), p2='ceres', units="l")  # Time passed in UTC
    getdist(time.time(), p1='sol', p2='saturn', units='l')