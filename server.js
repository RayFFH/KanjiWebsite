const express = require('express');
const fs = require('fs');
const axios = require('axios');
const app = express();
const port = 3000;
const path = require('path');
const mysql = require('mysql2'); 
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
function create_db_connection(host_name, user_name, user_password, db_name) {
    // Create a connection pool
    const pool = mysql.createPool({
        host: host_name,
        user: user_name,
        password: user_password,
        database: db_name,
        waitForConnections: true,
        connectionLimit: 10,
        queueLimit: 0
    });

    // Return the pool for reuse
    return pool.promise();
}

module.exports = create_db_connection;

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

app.post('/users', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Hash the password (using a secure method in production)
        const passwordHash = require('crypto').createHash('sha256').update(password).digest('hex');

        // Create a MySQL database connection
        const connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase");

        if (connection) {
            // Use the 'connection' object to execute the query
            const query = "INSERT INTO users (username, password_hash) VALUES (?, ?)";
            connection.query(query, [username, passwordHash], (err, results) => {
                if (err) {
                    console.error(err.message);
                    res.status(500).json({ error: 'Internal Server Error' });
                } else {
                    // results.insertId contains the last inserted ID
                    res.status(201).json({ message: 'User created successfully', userId: results.insertId });
                }
                // Close the database connection
                connection.end();
            });
        } else {
            res.status(500).json({ error: 'Internal Server Error' });
        }
    } catch (error) {
        console.error('An error occurred during user registration:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});
 
app.get('/getUser', (req, res) => {
    const username = req.query.username;

    if (!username) {
        return res.status(400).json({ error: 'Username parameter is required' });
    }

    // Create a database connection
    const connection = createDBConnection();

    // Connect to the database
    connection.connect();

    // Query to get user by username
    const query = 'SELECT * FROM users WHERE username = ?';

    // Execute the query
    connection.query(query, [username], (err, results) => {
        // Close the database connection
        connection.end();

        if (err) {
            return res.status(500).json({ error: 'Internal Server Error' });
        }

        if (results.length > 0) {
            // User found, return the user object
            return res.json(results[0]);
        } else {
            // User not found
            return res.status(404).json({ error: 'User not found' });
        }
    });
});


app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});