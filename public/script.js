// public/script.js
const currentPage = window.location.pathname;

// Add a condition to exclude the WaniKani page
if (currentPage !== '/wanikani.html') {
    // Your general code goes here
    console.log('Running script on non-WaniKani page');
    // ...

    // Example: Call functions or add general code
    // getRandomKanji();
} else {
    console.log('Script not running on WaniKani page');
}


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
                //hideAccountAndLoginBoxes();

                // Set the current user by username
                setCurrentUser(username);

                // Display a welcome message
                //displayWelcomeMessage(username); 
                document.getElementById('username-card-display').innerText = username;   
                const cardleveltext = document.getElementById('card-level-text');
                cardleveltext.classList.remove('hidden')
                //showLogoutButton();

                return username;
            } else {
                console.error('Failed to fetch user information:', response.statusText);
                return null;
            }
        } else {
            console.log('No user found.');
            //hideLogoutButton();
            return null;
        }
    } catch (error) {
        console.error('Error fetching user information:', error);
        return null;
    }
}


//document.addEventListener('DOMContentLoaded', getTokyoWeather);

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
        console.log('Random Sentence:', data.random_sentence);
            // Replace 'yourRandomKanjiVariable' with the actual variable storing the random kanji
        const randomKanji = data.random_kanji
        fetchAndDisplayNHKNews(randomKanji);
        
        


        // Assuming you have an element with the ID 'random-kanji' in your HTML
        const randomKanjiElement = document.getElementById('random-kanji');
        const randomSentenceElement = document.getElementById('random-sentence');

        // Display the fetched random kanji on the HTML element
        randomKanjiElement.setAttribute('data-kanji-info', JSON.stringify(data.random_kanji));

        randomKanjiElement.innerText = data.random_kanji[1];
        randomSentenceElement.innerText = data.random_sentence;

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
        showLogoutButton(); // Show logout button if a user is logged in
        } else {
        hideLogoutButton();
    }
    
}

function generateUniqueId() {
    const timestamp = new Date().getTime();
    const randomNum = Math.floor(Math.random() * 1000); // You can adjust the range as needed
    return `${timestamp}_${randomNum}`;
}

function loginSuccessful() {
    // Show the hidden elements
    document.getElementById('level-text').classList.remove('hidden');
    document.getElementById('buttons-container').classList.remove('hidden');
    // Other login-related logic
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

            loginSuccessful()
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

function logoutSuccessful() {
    // Hide the elements
    document.getElementById('level-text').classList.add('hidden');
    document.getElementById('buttons-container').classList.add('hidden');
    // Other logout-related logic
}
function logout() {
    // Clear the current user from local storage
    localStorage.removeItem('current_user');
    window.location.href = '/';

    // Optionally, redirect to the login or home page
    // window.location.href = '/login'; // Change the URL accordingly

    // Update the UI or perform any other necessary actions
    console.log('User logged out');
    logoutSuccessful()
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
        const currentUser = await getCurrentUser();
        if (currentUser) {
            console.log('yooooo');
            // Make a request to the server to save known kanji
            const response = await fetch('/saveKnownKanji', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: currentUser,  // Use the actual user ID here
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
        const currentUser = await getCurrentUser();
        if (currentUser) {
            // Make a request to the server to fetch known kanji
            console.log("current user now: " + currentUser)
            const response = await fetch(`/getKnownKanji?user_id=${currentUser}`, {
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

                knownKanjiCount = flattenedList.length

                // Get the current progress bar element
                
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
        const currentUser = await getCurrentUser();

        console.log(randomKanji)
        console.log(kanjiInfo + "kanjiinfo")
        console.log('Current User:', currentUser);
        
        const progressBar = document.getElementById('level-progress');

        // Get the current progress value from the progress bar
        let progress = parseInt(progressBar.style.width) || 0;

        // Increment the progress by 10% for each recognized kanji
        progress += 10;

        // Ensure the progress does not exceed 100%
        progress = Math.min(progress, 101);

        // Update the progress bar width
        progressBar.style.width = `${progress}%`;

        // If the level has increased, reset the progress bar
        if (progress > 100) {
            // Reset the progress bar
            progress = 0;
            progressBar.style.width = '0%';
        }


        if (currentUser) {
            // Make a request to the server to recognize and save known kanji
            console.log('Request Payload:', JSON.stringify({ user_id: currentUser, random_kanji: kanjiInfo }));


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
                    user_id: currentUser,
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
// async function dontRecognizeKanji() {
//     hideAccountAndLoginBoxes();
    
// }

async function dontRecognizeKanji() {
    //location.reload(); // Refresh the page
    await getRandomKanji();
    //hideAccountAndLoginBoxes();
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

async function showLogoutButton() {
    document.getElementById('level-text').classList.remove('hidden');
    document.getElementById('buttons-container').classList.remove('hidden');
}

// Function to hide the logout button and related elements
async function hideLogoutButton() {
    document.getElementById('level-text').classList.add('hidden');
    document.getElementById('buttons-container').classList.add('hidden');
}

async function updateLogoutButtonVisibility() {
    const userCardContainer = document.getElementById("user-card-container");
    const leveltext = document.getElementById('level-text');
    const logoutButton = document.getElementById('logoutButton');
    const loginButton = document.getElementById('loginButton');
    const wanikaniConnectButton = document.getElementById('wanikaniConnectButton');
    const createAccountButton = document.getElementById('createAccountButton');
    const currentuser = await getCurrentUser();
    if (currentuser) {
        logoutButton.classList.remove('hidden');
        loginButton.classList.add('hidden');
        createAccountButton.classList.add('hidden');
        //leveltext.classList.remove('hidden')
        userCardContainer.classList.remove("hidden");
        wanikaniConnectButton.classList.remove('hidden');
    } else {
        logoutButton.classList.add('hidden');
        loginButton.classList.remove('hidden');
        createAccountButton.classList.remove('hidden');
        userCardContainer.classList.add("hidden");
        wanikaniConnectButton.classList.add('hidden');
    }
}
// function displayNHKNews(newsData) {
//     const nhkNewsElement = document.getElementById('nhk-news');

//     // Display the NHK news data
//     nhkNewsElement.textContent = newsData;
// }

async function displayNHKNews(newsText, screenKanji) {
    const nhkNewsElement = document.getElementById('nhk-news');

    // Clear the existing content
    nhkNewsElement.innerHTML = '';

    // Split the news text into characters
    const newsCharacters = newsText.split('');
    console.log("HEHERHERHEHRDIOASDSASAD",screenKanji)

    // Create a new span element for each character
    newsCharacters.forEach((character) => {
        const span = document.createElement('span');
        span.textContent = character;

        // Check if the character is in the WaniKani kanji list
        if (screenKanji && Array.isArray(screenKanji) && screenKanji.includes(character)) {
            span.classList.add('highlight'); // Add a CSS class for highlighting
        }

        // Append the span element to the NHK news element
        nhkNewsElement.appendChild(span);
    });
}

// Function to fetch and display NHK news
async function fetchAndDisplayNHKNews(randomKanji, screenKanji) {
    try {
        // Make a GET request to the server to get NHK news based on the random kanji
        console.log("HERE" + randomKanji)
        const randomKan = randomKanji[1];
        console.log("YES" + randomKan)
        const response = await fetch(`/getNHKNews?randomKanji=${randomKan}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            // If the response is successful, parse the JSON data
            const newsData = await response.json();

            // Log the received news data for debugging
            console.log('Received NHK news data:', newsData);

            // Check if the NHK news story is empty, indicating no news found
            if (newsData.nhk_news_story === '') {
                console.log('No NHK news found.');
                // Handle this case as needed, e.g., display a message to the user
            } else {
                // Display NHK news at the bottom of the page
                displayNHKNews(newsData.article_text, screenKanji);
                console.log('Displayed NHK news successfully.');
            }
        } else {
            // If the response is not successful, log the error
            console.error('Failed to fetch NHK news:', response.statusText);
        }
    } catch (error) {
        // Handle any errors that occur during the fetch operation
        console.error('Error fetching NHK news:', error);
    }
}

function displayLoadingMessage(durationInSeconds) {
    const nhkNewsTitle = document.getElementById('nhk-news');

    // Set the initial loading message
    nhkNewsTitle.textContent = "Your Kanji related NHK News is loading...";

    // After the specified duration, clear the loading message
    setTimeout(() => {
        nhkNewsTitle.textContent = "NHK News"; // Replace with your actual NHK News title
    }, durationInSeconds * 1000); // Convert seconds to milliseconds
}

// Call the function with a delay of 7 seconds (adjust as needed)
displayLoadingMessage(11);

// Fetch and display NHK news when the page loads

// Call the function when the page loads to set initial visibility
updateLogoutButtonVisibility();

// Add event listeners to the Recognize and Don't Recognize buttons

