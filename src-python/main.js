async function getResultsJson(event) {
    event.preventDefault();

    const url = 'http://127.0.0.1:8000';  // Include protocol to ensure it's a full URL

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        /* 
        const jsonData = await response.json();  // Parse response as JSON
        console.log(jsonData);  // Access the JSON data here

        const calcOut = document.getElementById('calcOut');
        calcOut.innerHTML = JSON.stringify(jsonData, null, 2);  // Makes JSON output more readable
        */
       
    } catch (error) {
        console.error('Error fetching JSON data:', error);
        const calcOut = document.getElementById('calcOut');
        calcOut.innerHTML = 'Error loading data';
    }
}

function debug() {
    console.log('debugging...')
}

function setFormDate(id, date) {
    let formInp = document.getElementById(id);
    formInp.value = date;
}