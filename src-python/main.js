async function getResultsJson(event) {
    event.preventDefault();
    try {
        const response = await fetch("./results.json");
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        const jsonResult = await response.json();
        const calcOut = document.getElementById('calcOut');
        calcOut.innerHTML = JSON.stringify(jsonResult, null, 2); // Makes JSON output more readable
    } catch (error) {
        console.error("Error fetching JSON data:", error);
        const calcOut = document.getElementById('calcOut');
        calcOut.innerHTML = "Error loading data";
    }
}


function setFormDate(id, date) {
    let formInp = document.getElementById(id);
    formInp.value = date;
}