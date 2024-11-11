// Variables and Constants

let time = new Date();

let update = true;
let mult = 1;
let offset = 0;

const start = Date.now();

let id = setInterval(animate, 10);

let body = document.getElementById("body");
let title = document.getElementById("title");

// Functions

function generateFace(radius, offset, id){
  
  let face = document.getElementById(id);
  
  let left = face.style.left;
  let right = face.style.right;
  
  for(let i = 0; i < 60; i++){
    
    let posX = ((Math.cos((Math.PI / 30) * (i - 3) ) + 1) * (radius)) + offset;
    let posY = ((Math.sin((Math.PI / 30) * (i - 3) ) + 1) * (radius)) + offset;
    
    let char = '&#x25AA';
    
    if((i + 12) % 5 == 0) char = ((i + 12) / 5) % 12;
    if(char == 0) char = 12;
    
    face.innerHTML += '<div style="position: absolute; left:' + left + '; top: ' + top + '; transform: translate(' + posX + 'em,' + posY + 'em);">' + char + '</div';
    
  }
  
}

function analog(){
  
  let second = time.getSeconds();
  let minute = time.getMinutes() + (second / 60);
  let hour = time.getHours() + (minute / 60);
  
  let secondHand = document.getElementById("second");
  let minuteHand = document.getElementById("minute");
  let hourHand = document.getElementById("hour");
  
  let secondDeg = (second * 6) - 90
  let minuteDeg = (minute * 6) - 90
  let hourDeg = (hour * 30) - 90
  
  secondHand.style.transform = 'rotate(' + secondDeg + 'deg)';
  minuteHand.style.transform = 'rotate(' + minuteDeg + 'deg)';
  hourHand.style.transform = 'rotate(' + hourDeg + 'deg)';
  
}

function digital(){
  
  let digital = document.getElementById("digital");
  //let military = document.getElementById("military");
  
  let hour = time.getHours() % 12;
  if(hour == 0) hour = 12;
  if(hour < 10) hour = "0" + hour;
  
  let meridiem = "AM";
  if(time.getHours() >= 12) meridiem = "PM";
  
  let mHour = time.getHours();
  if(mHour < 10) mHour = "0" + mHour;
  
  let minute = time.getMinutes();
  if(minute < 10) minute = "0" + minute;
  
  let second = time.getSeconds();
  if(second < 10) second = "0" + second;
  
  digital.innerHTML = hour + ":" + minute + ":" + second + " " + meridiem;
  //military.innerHTML = mHour + ":" + minute + ":" + second;
  
}

function animate(){
  if (false);
  else {
    if (update) {
      time = new Date();
      time.setTime((time.getTime() * mult) + offset);
    }
    analog();
    digital();
  }
}
