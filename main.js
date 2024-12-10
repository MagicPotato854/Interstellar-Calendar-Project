// Define the hours offset from "year 1" to "1970"
const HOURS_OFFSET = 17327424;

// Sets the input field to the current UTC date and time in a readable format
function setCurrentDate() {
    const now = new Date();
    const formattedDate = now.toUTCString()
    document.getElementById("dateInput").value = formattedDate;
}

// Converts a flexible date-time string to hours since "year 1, January 1, 00:00:00"
function dateToHoursSinceEpoch(dateString) {
    const date = new Date(Date.parse(dateString)); 
    if (isNaN(date.getTime())) {
        alert("Invalid date format. Please use a format like 'Nov 9 2024 19:17:05'.");
        return null;
    }
    // Calculate hours since "year 1" by adding the offset
    const millisecondsSinceEpoch = date.getTime(); // Get milliseconds since epoch 
    const hoursSinceEpoch = millisecondsSinceEpoch / (1000 * 3600);
    return hoursSinceEpoch; // + HOURS_OFFSET
}

// Fetches the Earth and Mars times using the API
async function calculateTimes() {
    const dateString = document.getElementById("dateInput").value;
    const hours = dateToHoursSinceEpoch(dateString);

    if (hours === null) return; // Stop if the date is invalid

    try {
        console.log(`Fetching data for hours since "year 1": ${hours}`); // Debugging line

        // Fetch Earth time
        const earthResponse = await fetch(`http://localhost:5000/earth_time?hours=${hours}`);
        if (!earthResponse.ok) throw new Error(`HTTP error! status: ${earthResponse.status}`);
        const earthData = await earthResponse.json();

        // Fetch Mars time
        const marsResponse = await fetch(`http://localhost:5000/mars_time?hours=${hours}`);
        if (!marsResponse.ok) throw new Error(`HTTP error! status: ${marsResponse.status}`);
        const marsData = await marsResponse.json();


        const secs = hours * 3600; // Convert hours to seconds

        const distResponse = await fetch(`http://localhost:5000/dist?date=${secs}&p1=earth&p2=sun&units=l`);
        if (!distResponse.ok) throw new Error(`HTTP error! status: ${marsResponse.status}`);
        const distData = await distResponse.json()

        // Display results
        document.getElementById("results").innerHTML = `
            <p><strong>Earth Time:</strong> ${earthData.earth_time}</p>
            <p><strong>Mars Time:</strong> Year ${marsData.mars_year}, Day ${marsData.mars_day}, 
            ${marsData.hours}:${marsData.minutes}:${marsData.seconds} (${marsData.formatted_time})</p>
            <p>The distance between ${distData.p1} and ${distData.p2} is ${distData.distance}</p>
        `;
    } catch (error) {
        console.error("Error fetching data:", error);
        alert(`There was an error fetching the data: ${error.message}`);
    }
}

async function calcDistance() {
    const dataString = document.getElementById("dateInput").value;
    const secs = dateToHoursSinceEpoch(dataString) * 3600;

    const distResponse = await fetch(`http://localhost:5000/dist?date=${secs}?p1=earth?p2=sun?units=l`);
    if (!distResponse.ok) throw new Error(`HTTP error! status: ${marsResponse.status}`);
    const distData = await distResponse.json()
}
