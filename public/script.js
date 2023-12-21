// public/script.js
async function getCurrentUser() {
    try {
        const username = localStorage.getItem('current_user');
        if (username) {
            console.log('User found:', username);

            // Make a GET request to the server to get user information
            const response = await fetch(`/getUser?username=${username}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const userJSON = await response.json();
                console.log('User JSON:', userJSON);
                // Hide the account and login boxes
                hideAccountAndLoginBoxes();

                // Set the current user by username
                setCurrentUser(userJSON.username);

                // Display a welcome message
                displayWelcomeMessage(userJSON.username);    

                return userJSON.username;
            } else {
                console.error('Failed to fetch user information:', response.statusText);
                return null;
            }
        } else {
            console.log('No user found.');
            return null;
        }
    } catch (error) {
        console.error('Error fetching user information:', error);
        return null;
    }
}


document.addEventListener('DOMContentLoaded', getTokyoWeather);

document.addEventListener('DOMContentLoaded', function () {
    // Check if the user is already logged in
    //checkLoggedInUser();

    // generateRandomKanji();
    getRandomKanji();

    getKnownKanji();


});

async function getTokyoWeather() {
    try {
        const response = await fetch('/getWeather');
        const data = await response.json();

        console.log('Weather Data:', data);

        var weatherInfo = 'Temperature: ' + data.temperature.toFixed(2) + '°C, ' +
                          'Description: ' + data.description;
        document.getElementById('weather').innerText = weatherInfo;
    } catch (error) {
        console.error('Error fetching weather data:', error);
        document.getElementById('weather').innerText = 'Error fetching weather data. Please try again.';
    }
}
async function getRandomKanji() {
    try {
        const response = await fetch('/getRandomKanji');
        const data = await response.json();
        console.log('Random Kanji:', data.random_kanji);


        // Assuming you have an element with the ID 'random-kanji' in your HTML
        const randomKanjiElement = document.getElementById('random-kanji');

        // Display the fetched random kanji on the HTML element
        randomKanjiElement.setAttribute('data-kanji-info', JSON.stringify(data.random_kanji));

        randomKanjiElement.innerText = data.random_kanji[1];

        await getKnownKanji();
    } catch (error) {
        console.error('Error fetching random kanji data:', error);
        // Handle the error
    }
}
// Add the rest of your client-side JavaScript code here
// ...
async function checkLoggedInUser() {
    const currentUser = await getCurrentUser();
    console.log(currentUser)
    if (currentUser !== null && currentUser !== undefined) {
        console.log("This is the current user", currentUser)
        // Hide the account and login boxes
        hideAccountAndLoginBoxes();

        // Display a welcome message
        displayWelcomeMessage(currentUser.username);
    }
    
}

function generateUniqueId() {
    const timestamp = new Date().getTime();
    const randomNum = Math.floor(Math.random() * 1000); // You can adjust the range as needed
    return `${timestamp}_${randomNum}`;
}
// function storeUser(user) {

//     fetch('http://localhost:3000/api/users', {
//       method: 'POST',
//       headers: {
//          'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ user.username, password }),
//    })
//       .then(response => response.json())
//       .then(data => {
//          console.log(data);
//          alert('User registered successfully!');
//       })
//       .catch(error => {
//          console.error('Error:', error);
//          alert('Error registering user. Please try again.');
//       });
// });

//     try {
//         const response = await fetch('/storeUser');
//         const data = await response.json();
//         console.log('Stored User:', data.user);

//     } catch (error) {
//         console.error('Error getting the user data:', error);
//         // Handle the error
//     }
//     // Generate a unique user ID
//     //const userId = generateUniqueId();
    
//     // Attach the user ID to the user object
//     // user.id = userId;

//     // // Store the user in local storage using the user ID as the key
//     // localStorage.setItem(userId, JSON.stringify(user));

//     // Set the current user in local storage
//     setCurrentUser(userId);
// }

async function storeUser(username, password) {
    try {
        const response = await fetch('http://localhost:3000/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Stored User:', data.user);
        } else {
            console.error('Failed to store user:', response.statusText);
        }
    } catch (error) {
        console.error('Error getting the user data:', error);
        // Handle the error
    }
}

function createAccount() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    if (!usernameInput.value || !passwordInput.value) {
        alert('Username and password are required.');
        return;
    }

    // Check if the user already exists
    const existingUser = getUserByUsername(usernameInput.value);
    if (existingUser) {
        alert('User already exists. Please choose a different username.');
        return;
    }
    
    const newUser = {
        id: generateUniqueId(),
        username: usernameInput.value,
        password: passwordInput.value,
        recognizedKanji: [],
    };

    // Store the user in local storage
    storeUser(usernameInput.value, passwordInput.value);

    // Set the current user by user ID
    setCurrentUser(newUser.id);

    // Hide the account and login boxes
    hideAccountAndLoginBoxes();

    // Display a welcome message
    displayWelcomeMessage(newUser.username);
}


// Add the rest of your functions here
// ...
async function login() {
    const loginUsernameInput = document.getElementById('login-username');
    const loginPasswordInput = document.getElementById('login-password');

    // Basic validation
    if (!loginUsernameInput.value || !loginPasswordInput.value) {
        alert('Username and password are required.');
        return;
    }

    try {
        const response = await fetch('http://localhost:3000/getUserLogin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: loginUsernameInput.value,
                password: loginPasswordInput.value,
            }),
        });

        if (response.ok) {
            // Successfully logged in
            const data = await response.json();
            console.log('Login successful:', data.message);

            // Hide the account and login boxes
            hideAccountAndLoginBoxes();

            // Set the current user by username
            setCurrentUser(loginUsernameInput.value);

            // Display a welcome message
            displayWelcomeMessage(loginUsernameInput.value);
        } else if (response.status === 401) {
            // Invalid username or password
            alert('Invalid username or password. Please try again.');
        } else {
            console.error('Failed to login:', response.statusText);
        }
    } catch (error) {
        console.error('Error during login:', error);
    }
}
function hideAccountAndLoginBoxes() {
    const accountContainer = document.getElementById('account-container');
    const loginContainer = document.getElementById('login-container');

    // Hide both containers
    accountContainer.style.display = 'none';
    loginContainer.style.display = 'none';
}

// Function to display a welcome message
function displayWelcomeMessage(username) {
    const usernameDisplay = document.getElementById('username-display');
    usernameDisplay.textContent = 'Welcome, ' + username;
    usernameDisplay.style.display = 'block';
}
function getUserByUsername(username) {
    const userJSON = localStorage.getItem(username);
    return userJSON ? JSON.parse(userJSON) : null;
}


function setCurrentUser(username) {
    localStorage.setItem('current_user', username);
}
function logout() {
    // Clear the current user from local storage
    localStorage.removeItem('current_user');
    window.location.href = '/';

    // Optionally, redirect to the login or home page
    // window.location.href = '/login'; // Change the URL accordingly

    // Update the UI or perform any other necessary actions
    console.log('User logged out');
}

// function generateRandomKanji() {
//     const kanjiElement = document.getElementById('random-kanji');

//     // Fetch a random kanji from the Jisho API
//     fetch('https://jisho.org/api/v1/search/words?keyword=%23kanji')
//         .then(response => response.json())
//         .then(data => {
//             // Extract kanji information from the API response
//             const kanjiList = data.data.map(entry => entry.japanese[0].word);

//             // Get a random index from the kanjiList array
//             const randomIndex = Math.floor(Math.random() * kanjiList.length);

//             // Display the random kanji
//             kanjiElement.textContent = kanjiList[randomIndex];
//         })
//         .catch(error => {
//             console.error('Error fetching kanji data:', error);
//             kanjiElement.textContent = 'Error fetching kanji data. Please try again.';
//         });
// }
async function saveKnownKanji(kanji) {
    try {
        const currentUser = getCurrentUser();
        if (currentUser) {
            console.log('yooooo');
            // Make a request to the server to save known kanji
            const response = await fetch('/saveKnownKanji', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: currentUser.id,  // Use the actual user ID here
                    kanji: kanji,
                }),
            });

            if (response.ok) {
                console.log('Known kanji saved successfully.');
            } else {
                console.error('Failed to save known kanji:', response.statusText);
            }
        } else {
            alert('Please log in to save known kanji.');
        }
    } catch (error) {
        console.error('Error saving known kanji:', error);
    }
}

async function getKnownKanji() {
    try {
        const currentUser = getCurrentUser();
        if (currentUser) {
            // Make a request to the server to fetch known kanji
            //console.log(current)
            const response = await fetch(`/getKnownKanji?user_id=${currentUser.id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                console.log("Response was ok")
                const knownKanjiList = await response.json();
            
                console.log(knownKanjiList)
                // Extract an array of kanji from the list of objects
                const flattenedList = knownKanjiList.flat();

                // Log the flattened list for debugging
                console.log('flattenedList:', flattenedList);

                updateLevel(flattenedList.length);

                // Assuming you have an element with the ID 'known-kanji-list' in your HTML
                const knownKanjiListElement = document.getElementById('known-kanji-list');

                // Clear the existing content
                knownKanjiListElement.innerHTML = '';

                // Display the fetched known kanji on the HTML element
                flattenedList.forEach(knownKanji => {
                    const listItem = document.createElement('li');
                    listItem.textContent = knownKanji;
                    knownKanjiListElement.appendChild(listItem);
                });
            } else {
                console.error('Failed to fetch known kanji:', response.statusText);
            }

        }
    } catch (error) {
        console.error('Error fetching known kanji:', error);
    }
}

async function recognizeKanji() {
    try {
        // Assuming you have an element with the ID 'random-kanji' in your HTML
        const randomKanjiElement = document.getElementById('random-kanji');

        // Get the currently displayed random kanji
        const randomKanji = randomKanjiElement.textContent;

        const kanjiInfo = JSON.parse(randomKanjiElement.getAttribute('data-kanji-info'));

        // Get the current user
        const currentUser = getCurrentUser();

        console.log(randomKanji)
        console.log(kanjiInfo + "kanjiinfo")
        console.log('Current User:', currentUser);
        if (currentUser) {
            // Make a request to the server to recognize and save known kanji
            console.log('Request Payload:', JSON.stringify({ user_id: currentUser.id, random_kanji: kanjiInfo }));


            //Fetch a new random kanji
            await getRandomKanji();

            // Get the newly fetched random kanji
            const newRandomKanji = randomKanjiElement.textContent;


            const response = await fetch('/recognizeKanji', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: currentUser.id,
                    random_kanji: kanjiInfo,
                }),
            });
            console.log('Fetch Response:', response);

            if (response.ok) {
                console.log('Recognized kanji and updated known kanji list.');
                // Fetch and display the updated list of known kanji
                await getKnownKanji();
                console.log("Done")
            } else {
                console.error('Failed to recognize kanji:', response.statusText);
            }
        } else {
            alert('Please log in to recognize kanji.');
        }
    } catch (error) {
        console.error('Error recognizing kanji:', error);
    }
}

// Function to handle non-recognition of kanji
async function dontRecognizeKanji() {
    
}

function dontRecognizeKanji() {
    location.reload(); // Refresh the page
}

function updateLevel(knownKanjiCount) {
    // Your logic to update the level based on the knownKanjiCount
    // Example: Update the level every 10 known kanji
    const newLevel = Math.floor(knownKanjiCount / 10) + 1;
    console.log('New Level:', newLevel);

    // Update the level text on the UI
    const levelElement = document.getElementById('level');
    if (levelElement) {
        levelElement.textContent = newLevel;
    }
}


// Add event listeners to the Recognize and Don't Recognize buttons
document.getElementById('recognize-button').addEventListener('click', recognizeKanji);
document.getElementById('dont-recognize-button').addEventListener('click', dontRecognizeKanji);
