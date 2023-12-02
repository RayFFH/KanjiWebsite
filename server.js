const express = require('express');
const fs = require('fs');
const axios = require('axios');
const app = express();
const port = 3000;
const path = require('path');
//const { save_known_kanji, get_known_kanji } = require('./database');

app.use(express.json());
app.set('view engine', 'ejs'); // Set EJS as the view engine
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public'))); // Serve static files from the 'public' directory
app.use('/views', express.static(path.join(__dirname, 'views')));
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to read the API key
app.use((req, res, next) => {
    const filePath = 'API.txt';
    fs.readFile(filePath, 'utf8', (err, apiKey) => {
        if (err) {
            console.error('Error reading file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }
        req.apiKey = apiKey.trim();
        next();
    });
});

// Route to render the EJS file
app.get('/', (req, res) => {
    console.log('Rendering index.ejs');
    res.render('index', { apiKey: req.apiKey });
});

// Route to fetch weather data from the Python server
app.get('/getWeather', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/weather');
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        res.status(500).send('Internal Server Error');
    }
});
app.get('/getRandomKanji', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/getRandomKanji');
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching random kanji data:', error);
        res.status(500).send('Internal Server Error');
    }
});


app.post('/saveKnownKanji', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/saveKnownKanji', {
            user_id: req.body.user_id,
            kanji: req.body.kanji,
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error saving known kanji:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// app.get('/getKnownKanji', async (req, res) => {
//     try {
//         // const user_id = req.query.user_id;
//         // // const knownKanjiList = await get_known_kanji(user_id);
//         // // res.status(200).json(knownKanjiList);
//         const response = await axios.get('http://localhost:5000/getKnownKanji');
//         //console.log(response)
//         res.json(response.data);
//     } catch (error) {
//         console.error('Error fetching known kanji:', error);
//         res.status(500).json({ error: 'Internal Server Error' });
//     }
// });

app.get('/getKnownKanji', async (req, res) => {
    try {
        const user_id = req.query.user_id; // Retrieve user_id from query parameters
        const response = await axios.get(`http://localhost:5000/getKnownKanji?user_id=${user_id}`);
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching known kanji:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.post('/recognizeKanji', async (req, res) => {
    try {
        // Assuming you have an element with the ID 'random-kanji' in your HTML
        // const randomKanjiElement = document.getElementById('random-kanji');
    
        // Get the currently displayed random kanji
        // const randomKanji = randomKanjiElement.textContent;
    
        // Make a request to the server to recognize and save known kanji
        const response = await axios.post('http://localhost:5000/recognizeKanji', {
            user_id: req.body.user_id,  // Replace with the actual user ID
            random_kanji: req.body.random_kanji,
        });

        try {
            if (response.status === 200) {
                const knownKanjiList = response.data;
                //const actualKanjiList = knownKanjiList.kanji;
                console.log('Recognized kanji and updated known kanji list:', knownKanjiList);
    
                // Assuming you want to update the UI with the known kanji list
                // You can replace this part with your UI update logic
                // For example, updating a list on the web page
                // const knownKanjiListElement = document.getElementById('known-kanji-list');
                // knownKanjiListElement.innerHTML = '';
                // knownKanjiList.forEach(knownKanji => {
                    // try {
                    //     const listItem = document.createElement('li');
                    //     listItem.textContent = knownKanji.kanji;
                    //     knownKanjiListElement.appendChild(listItem);
                    // } catch (innerError) {
                    //     console.error('Error updating UI with known kanji:', innerError);
                    // }
                // });
                res.json(knownKanjiList);

            } else {
                console.error('Failed to recognize kanji:', response.statusText);
                // Handle the error, e.g., display an error message to the user
            }
        } catch (error) {
            console.error('Error handling response:', error);
        }
    } catch (error) {
        console.error('Error recognizing kanji:', error);
        // Handle the error, e.g., display an error message to the user
    }
});


app.post('/dontRecognizeKanji', async (req, res) => {
    // Implement the logic for non-recognition of kanji
    // ...
});
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});