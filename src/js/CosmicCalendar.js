// Set

stat.style.backgroundColor = "rgb(128, 255, 128)";
stat.innerHTML = "Awaiting Input";

render();

// Variables and Constants

let timeA = new Date();
let timeB = new Date();

// Functions

function setFormDate(id, date) {
  
  let formInp = document.getElementById(id)
  
  formInp.value = date;
  
}

// Objects



// Inp Form

document.getElementById("valFormA").addEventListener("submit", function (event) {
  
  event.preventDefault();
  
  // Values
  
  let timeInp = document.getElementById("timeA").value;
  
  let time = new Date(timeInp);
  setFormDate('timeA', time);
  
  print_planet_time(date_to_mars(time));
  
  stat.style.backgroundColor = "rgb(128, 255, 128)";
  stat.innerHTML = "Calculated";
  
});
