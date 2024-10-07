
function date_to_mars(date) {
    /*
    We are going to use a proposed Martian Calendar that is extremely accurate.
    A year changes between 668 and 669 days. A "Leap Year" occurs every odd
    year, every year divisable by ten but not divisable by 100. Accepts the date object in js.
    */
    let year = 0;
    hours = (date.getTime() + 62135596800000) / 3600000
    while (hours >= 16497.4731) {
        year += 1;
        if ((year % 2 != 0 || year % 10 == 0) && year % 100 != 0) {
            hours -= 16497.4731;
        } else {
            hours -= 16472.8132;
        }
    }
    let day = Math.floor(hours/24.6599);
    hours -= day * 24.6599;
    let leftovers = hours % 1;
    hours -= leftovers;
    let minutes = Math.floor(leftovers * 60);
    leftovers -= minutes / 60;
    let seconds = leftovers * 3600;

    return [year + 1, parseInt(day + 1), parseInt(hours), minutes, Math.round(seconds/3)];
}

function print_planet_time(date) {
    /*
    Prints a date in human readable format.
    date should be a tuple formatted like the following:
    (year, day, hours, minutes, seconds)
    */
   out = (`Year ${date[0]}, day ${date[1]}, ${date[2]}:${date[3]}:${date[4]}`);
   
   console.log(out);
   
   calcOut = document.getElementById("calcOut");
   
   calcOut.innerHTML = out;
   
}

let date = new Date();
print_planet_time(date_to_mars(date));
console.log(date);