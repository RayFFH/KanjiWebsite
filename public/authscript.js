// public/authscript.js
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
                //showLogoutButton();

                return username;
            } else {
                console.error('Failed to fetch user information:', response.statusText);
                return null;
            }
        } else {
            console.log('No user found.');
            hideLogoutButton();
            return null;
        }
    } catch (error) {
        console.error('Error fetching user information:', error);
        return null;
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
        //hideAccountAndLoginBoxes();

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
    // document.getElementById('level-text').classList.remove('hidden');
    // document.getElementById('buttons-container').classList.remove('hidden');
    // Other login-related logic
    window.location.href = '/';
}

async function storeUser(username, password) {
    console.log('Stored User:', username);
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
            console.log('Stored data:', data);
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
    //hideAccountAndLoginBoxes();

    // Display a welcome message
    //displayWelcomeMessage(newUser.username);
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
            //hideAccountAndLoginBoxes();

            // Set the current user by username
            setCurrentUser(loginUsernameInput.value);

            // Display a welcome message
            //displayWelcomeMessage(loginUsernameInput.value);

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




async function showLogoutButton() {
    document.getElementById('level-text').classList.remove('hidden');
    document.getElementById('buttons-container').classList.remove('hidden');
}

// Function to hide the logout button and related elements
async function hideLogoutButton() {
    document.getElementById('level-text').classList.add('hidden');
    document.getElementById('buttons-container').classList.add('hidden');
}

function loginSuccessful() {
    // Show the hidden elements
    // document.getElementById('level-text').classList.remove('hidden');
    // document.getElementById('buttons-container').classList.remove('hidden');

    // Redirect to the main page after successful login
    window.location.href = '/'; // Update with your main page URL
}

// Function to handle successful account creation
function createAccountSuccessful() {
    // Show the hidden elements
    document.getElementById('level-text').classList.remove('hidden');
    document.getElementById('buttons-container').classList.remove('hidden');

    // Redirect to the main page after successful account creation
    window.location.href = '/main-page.html'; // Update with your main page URL
}



