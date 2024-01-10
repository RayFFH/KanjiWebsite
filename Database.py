import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "349dsahoDSI3:",
    database= "testdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Temp2(name VARCHAR(50), temp smallint UNSIGNED, tempID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE Temp")
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def table_insert(connection,name1, temp1):
    mycursor = connection.cursor()
    mycursor.execute("INSERT INTO Temp2(name,temp) VALUES (%s,%s)",(name1,temp1))
    connection.commit()
# for x in mycursor:
#     print(x)
def table_select(connection, table_name):
    try:
        mycursor = connection.cursor()
        query = f"SELECT * FROM {table_name}"
        mycursor.execute(query)
        
        # Assuming you want to return the result as a list of rows
        result = [row for row in mycursor]

        return result
    except Exception as e:
        # Handle exceptions appropriately (print, log, or raise)
        print(f"Error in table_select: {e}")
        return None
def save_known_kanji(connection, user_id, kanji):
    success = False  # Initialize the success indicator
    try:
        if kanji is not None:
            cursor = connection.cursor()

            kanji = ', '.join(map(str, kanji))

            # Define the SQL query to insert data into the table
            insert_query = """
            INSERT INTO known_kanji (user_id, kanji) VALUES (%s, %s);
            """

            # Execute the query with user_id and kanji as parameters
            cursor.execute(insert_query, (user_id, kanji))

            # Commit the changes
            connection.commit()

            print(f"Saved kanji: {kanji}")
            success = True  # Indicate success
        else:
            print("Ignoring null kanji.")
    except Exception as e:
        print(f"An error occurred while saving kanji: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return success  # Return the success indicator

def get_known_kanji(connection, user_id):
    try:
        if not connection.is_connected():
            connection.reconnect()  # Attempt to reconnect if not open
            if not connection.is_connected():
                print("MySQL Connection is not open.")
                return []
        
        cursor = connection.cursor()
        print("We are here right now in the databse" + user_id)
        # Define the SQL query to fetch known kanji for a specific user

        
        # select_query = """
        # SELECT kanji FROM known_kanji WHERE user_id = %s;
        # """
        select_query = """
        SELECT DISTINCT kanji FROM known_kanji WHERE user_id = %s;
        """

        # Execute the query with the user_id as a parameter
        cursor.execute(select_query, (user_id,))

        # Fetch all rows (kanji) from the result set
        known_kanji_list = cursor.fetchall()

        # Print a message to indicate that the query was successful
        print("Query executed successfully")

        # Iterate over the result and print each kanji
        for row in known_kanji_list:
            kanji = row[0]
            print(f'Kanji: {kanji}')

        return known_kanji_list

    except Exception as e:
        print(f"An error occurred while fetching known kanji: {e}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()