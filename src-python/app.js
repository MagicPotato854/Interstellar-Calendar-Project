const express = require('express');
const bodyParser = require('body-parser');
const { spawnSync } = require('child_process');
const { readFile } = require('fs/promises');
const { appendFile } = require('fs/promises');
const { join } = require('path');
const { time } = require('console');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", async (req, res, next)=>{
    const X = [1,2, 5]; // large array
    const y = [[1,2], [2,3], [1,2]]; // large array
    const date = new Date();
    const current_time = (date.getTime() + 62135596800000) / 3600000;
    const planet_name = 'Saturn';

    await appendFile(
            join(`/Users/kohlerm/Repository/Interstellar-Calendar-Project/src-python/args.json`),
            JSON.stringify({ X, y, current_time, planet_name }),
            {
                encoding: 'utf-8',
                flag: 'w',
            },
        );
    const pythonProcess = await spawnSync('python3', [
     '/Users/kohlerm/Repository/Interstellar-Calendar-Project/src-python/python-script.py',
     'calculate',
     '/Users/kohlerm/Repository/Interstellar-Calendar-Project/src-python/args.json',
     '/Users/kohlerm/Repository/Interstellar-Calendar-Project/src-python/results.json'
    ]);
    const result = pythonProcess.stdout?.toString()?.trim();
    const error = pythonProcess.stderr?.toString()?.trim();

    const status = result === 'OK';
    if (status) {
        const buffer = await readFile('/Users/kohlerm/Repository/Interstellar-Calendar-Project/src-python/results.json');
        const resultParsed = JSON.parse(buffer?.toString());
        res.send(resultParsed.toString())
    } else {
        console.log(error)
        res.send(JSON.stringify({ status: 500, message: 'Server error' }))
        // document.getElementById('calcOut').textContent = "Error"
    }
});

// Creates the server on default port 8000 and can be accessed through localhost:8000
const port=8000;
app.listen(port, () => console.log(`Server is listening on PORT ${port}`));