// your-database-module.js

// Assuming you have a create_db_connection function to establish a database connection

const mysql = require('mysql2/promise'); 

async function getUserByUsername(username) {
    const connection = create_db_connection("localhost", "root", "349dsahoDSI3:", "testdatabase");

    

    if (connection) {
        // Implement logic to query the database for the user by username
        // ...

        // For example, you might use a SQL query to fetch the user
        const query = "SELECT * FROM users WHERE username = ?";
        const [user] = await connection.execute(query, [username]);

        connection.close();

        return user;
    } else {
        // Handle the case where the database connection fails
        return null;
    }
}



async function create_db_connection(host_name, user_name, user_password, db_name) {
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

module.exports = {
    getUserByUsername,
};
