from flask import Flask, jsonify, render_template, request
import requests
from random import choice
from Database import table_select, create_db_connection,save_known_kanji, get_known_kanji
from flask_cors import CORS
import random
import hashlib
from kanji_templates import kanji_templates
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
# import pymysql

app = Flask(__name__,template_folder='public')
CORS(app) 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('API.txt', 'r').readline()
CITY = 'TOKYO'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_random_sentence_for_kanji(kanji):
    # Check if the kanji is in the templates
    if kanji in kanji_templates:
        # Get the templates for the specified kanji
        templates_for_kanji = kanji_templates[kanji]
        
        # Pick a random sentence from the templates
        random_sentence = random.choice(templates_for_kanji)
        
        return random_sentence
    else:
        return "No templates available for this kanji."

def get_username_by_id(user_id):
    # Establish a database connection
    connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")

    try:
        with connection.cursor() as cursor:
            print("Retrieving usernmae" + user_id)
            # Execute the SQL query to retrieve the username by user_id
            # sql = "SELECT username FROM users WHERE id = %s"
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()

            if result:
                print("the user returned")
                print(result[1])
                return result[1]  # Return the username
            else:
                print("no user")
                return None  # User not found
    except Exception as e:
        print(f"Error in get_username_by_id: {e}")
        return None
    finally:
        connection.close()

@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        # Fetch weather data
        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius = kelvin_to_celsius(temp_kelvin)

        # Retrieve random kanji from the database
        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")
        kanji_list = table_select(connection, "kanji")
        random_kanji = choice(kanji_list)

        # Render the HTML template with weather information and random kanji
        # return render_template('public/index.html', weather={
        #     'temperature': temp_celsius,
        #     'description': response['weather'][0]['description']
        # }, random_kanji=random_kanji)
        return jsonify({
        'temperature': temp_celsius,
        'description': response['weather'][0]['description']
    })
    except Exception as e:
        # Log the exception for further analysis
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/getWeather', methods=['GET'])
def get_weather_api():
    # Fetch weather data
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    # Return weather data as JSON
    return jsonify({
        'temperature': temp_celsius,
        'description': response['weather'][0]['description']
    })

@app.route('/getRandomKanji', methods=['GET'])
def get_random_kanji_api():
    try:
        # Retrieve all kanji from the database
        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")
        kanji_list = table_select(connection, "kanji")

        # Choose a random kanji from the list
        random_kanji = random.choice(kanji_list)

        random_sentence = get_random_sentence_for_kanji(random_kanji[1])

        # Return random kanji data as JSON
        return jsonify({'random_kanji': random_kanji, 'random_sentence': random_sentence})
    except Exception as e:
        # Log the exception for further analysis
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/saveKnownKanji', methods=['POST'])
def save_known_kanji_route():
    try:
        if request.headers['Content-Type'] == 'application/json':
            # Get user_id and kanji from the request
            user_id = request.json.get('user_id')
            kanji = request.json.get('kanji')

            # Save known kanji to the database
            connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")
            save_known_kanji(connection, user_id, kanji)

            return jsonify({'success': True}), 200
        else:
            return jsonify({'error': 'Unsupported Media Type'}), 415
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
@app.route('/getKnownKanji', methods=['GET'])
def get_known_kanji_route():
    try:
        # Get user_id from the request
        user_id = request.args.get('user_id')
        print("knownkanjiuserid" + user_id)
        # Fetch known kanji from the database
        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")
        known_kanji_list = get_known_kanji(connection, user_id)

        # Return the list of known kanji
        #print(known_kanji_list)
        return jsonify(known_kanji_list), 200
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/recognizeKanji', methods=['POST'])
def recognize_kanji_route():
    try:
        # Log the received request body
        print(request.json)

        user_id = request.json.get('user_id')
        print(f"Received user_id: {user_id}")
        # Get user_id from the request
        # Assuming you have an element with the ID 'random-kanji' in your HTML
        random_kanji = request.json.get('random_kanji')
        print(f"Received random_kanji: {random_kanji}")

        # Save the recognized kanji to the database
        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")
        if connection:
            # Save the recognized kanji to the database
            with connection:
                save_known_kanji(connection, user_id, random_kanji)
            print("Now getting kanji")
            # Fetch and return the updated list of known kanji
            known_kanji_list = get_known_kanji(connection, user_id)
            print("Got known kanji:", known_kanji_list)
            return jsonify(known_kanji_list), 200
        else:
            return jsonify({'error': 'Database Connection Failed'}), 500

    except Exception as e:
        # Log the exception for further analysis
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
    

@app.route('/users', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print("Trying to creater user")
        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")

        if connection:
            cursor = connection.cursor()

            # Hash the password (using a secure method in production)
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Insert user into the database
            query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
            cursor.execute(query, (username, password_hash))

            connection.commit()
            cursor.close()
            connection.close()

            return jsonify(message='User created successfully', user_id=cursor.lastrowid), 201
        else:
            return jsonify(error='Internal Server Error'), 500
    except Exception as e:
        print(f"An error occurred during user registration: {e}")
        return jsonify(error='Internal Server Error'), 500

@app.route('/getLogin', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase")

        if connection:
            cursor = connection.cursor()

            # Hash the provided password for comparison
            password_hash = hashlib.sha256(password.encode()).hexdigest()
    
            # Check if the user exists in the database
            query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
            cursor.execute(query, (username, password_hash))

            user = cursor.fetchone()

            if user:
                cursor.close()
                connection.close()
                return jsonify(message='Login successful'), 200
            else:
                cursor.close()
                connection.close()
                return jsonify(error='Invalid username or password'), 401
        else:
            return jsonify(error='Internal Server Error'), 500
    except Exception as e:
        print(f"An error occurred during user login: {e}")
        return jsonify(error='Internal Server Error'), 500
    

@app.route('/getUsername', methods=['GET'])
def get_username():
    # Get the user_id from the request parameters
    user_id = request.args.get('username')
    print("here"+ user_id)
    if user_id is not None:
        # Call the function to get the username
        username = get_username_by_id(user_id)

        if username is not None:
            return jsonify(username=username)
        else:
             return jsonify(message='User not found'), 200 
    else:
        return jsonify(error='Missing user_id parameter'), 400
    
def get_nhk_article(kanji):
    try:
        # NHK Easy News URL with the current kanji
        nhk_url = f'https://www3.nhk.or.jp/news/nsearch/?col=news&charset=utf-8&qi=3&qt={kanji}'

        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode

        # Create a new instance of the Chrome driver with headless options
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the NHK Easy News URL
        driver.get(nhk_url)

        # Wait for some time to let the page load (adjust as needed)
        time.sleep(5)

        # Get the page source after JavaScript has executed
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the section with class "search--items"
        search_items_section = soup.find('section', class_='search--items')

        if search_items_section:
            # Find all list items within the section
            list_items = search_items_section.find_all('li')

            # Extract and concatenate the text from each search note
            article_text = '\n'.join([item.find('p', class_='search-note').get_text(strip=True) if item.find('p', class_='search-note') else '' for item in list_items])

            return article_text.strip()  # Strip leading/trailing whitespaces
        else:
            return "No search items found on the page."

    except Exception as e:
        print(f"An error occurred during NHK Easy News scraping: {str(e)}")
        return "Failed to retrieve NHK Easy News article."

    finally:
        # Close the browser window
        driver.quit()

@app.route('/getNHKNews', methods=['GET'])
def get_nhk_article_route():
    try:
        # Get the kanji from the request parameters
        kanji = request.args.get('current_kanji')

        # Call the function to get the NHK Easy News article
        article_text = get_nhk_article(kanji)

        # Return the NHK Easy News article text as JSON
        return jsonify({'article_text': article_text})
    except Exception as e:
        print(f"An error occurred during NHK Easy News retrieval: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

# ... (rest of your code)

if __name__ == '__main__':
    app.run(port=5000)