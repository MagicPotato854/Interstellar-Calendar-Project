// Variables

const stat = document.getElementById("stat");
stat.style.backgroundColor = "rgb(255, 255, 128)";
stat.innerHTML = "Loading Data...";

// Class

class celestial {
  
  constructor(name, parent, sMajorA, sMinorA, radius, inclination, orbPeriod, orbStart, revPeriod, revStart, startDate, meanLongitude, perihelion, LAN, xOffset, colour, fontColour, fontSize) {
    
    this.name = name;
    this.parent = parent;
    this.sMajorA = sMajorA;
    this.sMinorA = sMinorA;
    this.radius = radius;
    this.inclination = inclination;
    this.orbPeriod = orbPeriod;
    this.orbStart = orbStart;
    this.revPeriod = revPeriod;
    this.revStart = revStart;
    this.startDate = startDate;
    this.meanLongitude = meanLongitude;
    this.perihelion = perihelion;
    this.LAN = LAN;

    createCelestial(radius, sMajorA, xOffset, name, colour, fontColour, fontSize);
    
  }
  
}

// Data

createCelestial(695500, 0, 0, 'Sun', '#FFF0D0', '#000000', 0.7);
createCelestial(2240, 57896064, 0, 'Mercury', '#808080', '#FFFFFF', 0.5);
createCelestial(6052, 108168050, 0, 'Venus', '#F0E0C0', '#000000', 0.5);
createCelestial(6371, 149597871, 0, 'Earth', '#008040', '#FFFFFF', 0.5);
createCelestial(1737.5, 385000, 149597871, 'Moon', '#C0C0C0', '#000000', 0.5);
createCelestial(3390, 227893510, 0, 'Mars', '#C04020', '#FFFFFF', 0.5);
createCelestial(11.1, 9375, 227893510, 'Phobos', '#808080', '#FFFFFF', 0.5);
createCelestial(6.2, 23458, 227893510, 'Deimos', '#C08080', '#FFFFFF', 0.5);
createCelestial(392, 414006270, 0, 'Ceres', '#606080', '#FFFFFF', 0.5);
createCelestial(69911, 777957370, 0, 'Jupiter', '#C0B060', '#FFFFFF', 0.5);
createCelestial(21.5, 127842, 777957370, 'Metis', '#A0A080', '#FFFFFF', 0.5);
createCelestial(8.2, 128766, 777957370, 'Adrastea', '#A09060', '#FFFFFF', 0.5);
createCelestial(83.4, 181396, 777957370, 'Amalthea', '#A09060', '#FFFFFF', 0.5);
createCelestial(49.3, 217991, 777957370, 'Thebe', '#A09060', '#FFFFFF', 0.5);
createCelestial(1822, 421799, 777957370, 'Io', '#D0A040', '#FFFFFF', 1);
createCelestial(1561, 671098, 777957370, 'Europa', '#A0A0C0', '#000000', 0.5);
createCelestial(2631, 1070404, 777957370, 'Ganymede', '#A08080', '#FFFFFF', 0.4);
createCelestial(2410, 1882638, 777957370, 'Callisto', '#808080', '#FFFFFF', 0.5);
createCelestial(58232, 1428070100, 0, 'Saturn', '#C0C060', '#FFFFFF', 0.5);
createCelestial(198, 185538, 1428070100, 'Mimas', '#A0A0A0', '#FFFFFF', 0.5);
createCelestial(252, 238041, 1428070100, 'Enceladus', '#8080A0', '#FFFFFF', 0.4);
createCelestial(522, 294672, 1428070100, 'Tethys', '#A0A0A0', '#FFFFFF', 0.5);
createCelestial(562, 377415, 1428070100, 'Dione', '#A0A0A0', '#FFFFFF', 0.5);
createCelestial(764, 527067, 1428070100, 'Rhea', '#A0A080', '#FFFFFF', 0.5);
createCelestial(2575, 1221865, 1428070100, 'Titan', '#B08040', '#FFFFFF', 0.5);
createCelestial(736, 3560841, 1428070100, 'Iapetus', '#A0A0A0', '#FFFFFF', 0.5);
createCelestial(25362, 2871452300, 0, 'Uranus', '#80B0B0', '#FFFFFF', 0.5);
createCelestial(236, 129893, 2871452300, 'Miranda', '#A0A080', '#FFFFFF', 0.5);
createCelestial(579, 190896, 2871452300, 'Ariel', '#A0A080', '#FFFFFF', 0.5);
createCelestial(585, 266016, 2871452300, 'Umbriel', '#A0A080', '#FFFFFF', 0.5);
createCelestial(789, 436291, 2871452300, 'Titania', '#A0A080', '#FFFFFF', 0.5);
createCelestial(761, 583428, 2871452300, 'Oberon', '#A0A080', '#FFFFFF', 0.5);
createCelestial(24622, 4502141500, 0, 'Neptune', '#4040B0', '#000000', 0.5);

// Functions



// Class


