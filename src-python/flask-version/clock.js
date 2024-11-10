const earthClockCanvas = document.getElementById("earthClock").getContext("2d");
const marsClockCanvas = document.getElementById("marsClock").getContext("2d");
const HOURS_OFFSET = 17327424; // Hours from "year 1" to 1970

// Function to get Earth time locally using JavaScript Date object
function getCurrentEarthTime() {
    const now = new Date();
    return [now.getHours(), now.getMinutes(), now.getSeconds()];
}

// Function to calculate total hours since "year 1" up to the current UTC time
function calculateCurrentHoursSinceYear1() {
    const now = new Date();
    const millisecondsSinceEpoch = now.getTime();
    const millisecondsSinceYear1 = millisecondsSinceEpoch + HOURS_OFFSET * 3600 * 1000;
    return millisecondsSinceYear1 / (1000 * 3600); // Convert milliseconds to hours
}

// Function to draw the clock on the canvas
function drawClock(ctx, hours, minutes, seconds) {
    ctx.clearRect(0, 0, 200, 200); // Clear the canvas
    ctx.beginPath();
    ctx.arc(100, 100, 90, 0, 2 * Math.PI); // Draw clock face
    ctx.stroke();

    // Calculate and draw hour hand
    const hourAngle = (hours % 24 + minutes / 60) * (2 * Math.PI / 24);
    drawHand(ctx, hourAngle, 50, "black");

    // Calculate and draw minute hand
    const minuteAngle = (minutes + seconds / 60) * (2 * Math.PI / 60);
    drawHand(ctx, minuteAngle, 70, "black");

    // Calculate and draw second hand
    const secondAngle = seconds * (2 * Math.PI / 60);
    drawHand(ctx, secondAngle, 80, "red");
}

// Helper function to draw individual clock hands
function drawHand(ctx, angle, length, color) {
    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(100 + length * Math.cos(angle - Math.PI / 2), 100 + length * Math.sin(angle - Math.PI / 2));
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.stroke();
}

// Function to update Earth clock using local time
function updateEarthClock() {
    const [hours, minutes, seconds] = getCurrentEarthTime();
    drawClock(earthClockCanvas, hours, minutes, seconds);
}

// Fetch and draw Mars clock from the API
async function fetchAndDrawMarsClock() {
    const hoursSinceYear1 = calculateCurrentHoursSinceYear1();
    try {
        const response = await fetch(`http://localhost:5000/mars_time?hours=${hoursSinceYear1}`);
        const data = await response.json();
        
        console.log("Mars time response:", data);  // Log response for debugging
        const { hours, minutes, seconds } = data;  // Use Mars hours, minutes, seconds directly
        drawClock(marsClockCanvas, hours, minutes, seconds);
    } catch (error) {
        console.error("Error fetching Mars time:", error);
    }
}

// Unified function to update both clocks
function updateClocks() {
    updateEarthClock();  // Update Earth clock using JavaScript Date object
    fetchAndDrawMarsClock();  // Update Mars clock by fetching from the API
}

// Update clocks every second
setInterval(updateClocks, 1000);
