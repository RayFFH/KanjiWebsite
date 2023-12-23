const express = require('express');
const fs = require('fs');
const axios = require('axios');
const app = express();
const port = 3000;
const path = require('path');
const mysql = require('mysql2'); 
const bodyParser = require('body-parser');
const crypto = require('crypto');
//const { save_known_kanji, get_known_kanji } = require('./database');

//const { getUserByUsername } = require('./database-module');

const cors = require('cors');
app.use(cors());
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
        const { random_kanji, random_sentence } = response.data;
        res.json({ random_kanji, random_sentence });
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


app.get('/getUser', async (req, res) => {
    const username = req.query.username;

    // Send a request to the Python server to get the username
    try {
        const pythonResponse = await axios.get(`http://localhost:5000/getUsername?username=${username}`);
        
        if (pythonResponse.status === 200) {
            const pythonUsername = pythonResponse.data;
            console.log('Username from Python:', pythonUsername);

            res.status(200).json({ username: pythonUsername });
        } else {
            console.error('Failed to fetch username from Python:', pythonResponse.statusText);
            res.status(500).json({ error: 'Internal Server Error' });
        }
    } catch (error) {
        console.error('Error fetching username from Python:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.post('/getUserLogin', async (req, res) => {
    const username = req.body.username;
    const password = req.body.username;

    // Send a request to the Python server to get the username
    try {
        const pythonResponse = await axios.post(`http://localhost:5000/getLogin`, {
            username,
            password,
        });
        
        if (pythonResponse.status === 200) {
            const pythonUsername = pythonResponse.data;
            console.log('Username from Python:', pythonUsername);

            res.status(200).json({ username: pythonUsername });
        } else {
            console.error('Failed to fetch username from Python:', pythonResponse.statusText);
            res.status(500).json({ error: 'Internal Server Error' });
        }
    } catch (error) {
        console.error('Error fetching username from Python:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// app.post('/login', (req, res) => {
//     const connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase");

//     const { username, password } = req.body;

//     // Hash the password (using a secure method in production)
//     const passwordHash = crypto.createHash('sha256').update(password).digest('hex');
  
//     // Check if the user exists
//     const query = 'SELECT * FROM users WHERE username = ? AND password_hash = ?';
//     connection.query(query, [username, passwordHash], (err, results) => {
//       if (err) {
//         console.error('Error executing login query:', err);
//         res.status(500).json({ error: 'Internal Server Error' });
//       } else {
//         if (results.length > 0) {
//           // User authenticated successfully
//           res.status(200).json({ message: 'Login successful', user: results[0] });
//         } else {
//           // Incorrect username or password
//           res.status(401).json({ error: 'Invalid username or password' });
//         }
//       }
  
//       // Close the connection after the query is done
//       connection.end();
//     });
//   });

app.post('/users', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Make a request to the Python Flask function for user authentication
        const pythonResponse = await axios.post('http://localhost:5000/users', {
            username,
            password,
        });

        // Forward the response from the Python Flask function to the client
        res.status(pythonResponse.status).json(pythonResponse.data);
    } catch (error) {
        console.error('Error during login:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// async function getUserByUsername(username) {
//     const connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase");

    

//     if (connection) {
//         // Implement logic to query the database for the user by username
//         // ...

//         // For example, you might use a SQL query to fetch the user
//         const query = "SELECT * FROM users WHERE username = ?";
//         const [user] = await connection.execute(query, [username]);

//         connection.end();

//         return user;
//     } else {
//         // Handle the case where the database connection fails
//         return null;
//     }
// }
app.get('/getNHKNews', async (req, res) => {
    try {
        // Assuming you have the current kanji available in req.query.current_kanji
        const currentKanji = req.query.randomKanji;
        console.log("HERHERHEHSHHERRHE"+ currentKanji)
        // Make a GET request to the Flask server to get NHK news
        const response = await axios.get(`http://localhost:5000/getNHKNews?current_kanji=${currentKanji}`);

        // Forward the NHK news data to the client
        res.status(response.status).json(response.data);
    } catch (error) {
        console.error('Error fetching NHK news:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});



app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});