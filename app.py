from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import bcrypt

app = Flask(__name__)

# Function to establish a database connection
def connect_to_db():
    try:
        conn = psycopg2.connect(
            database="manishak",
            user="manishak",
            password="j*hp6y6dSy",
            host="db.cecs.pdx.edu",
            port="5432"
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to the database:", error)
        return None

# Function to create the "users" table in the database
def create_users_table(conn):
    try:
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while creating the table:", error)

# Function to register a new user
def register_user(conn, username, first_name, last_name, email, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Define the query and its parameters
            insert_user_query = """
                INSERT INTO se_project.users (username, first_name, last_name, email, password)
                VALUES (%s, %s, %s, %s, %s)
            """
            query_params = (username, first_name, last_name, email, hashed_password)

            # Execute the query
            cursor.execute(insert_user_query, query_params)

            conn.commit()
            cursor.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while registering the user:", error)
        finally:
            conn.close()
    return False

# Function to handle user login
def login_user(email, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Query the database to get the stored hashed password
            get_password_query = "SELECT password FROM se_project.users WHERE email = %s"
            cursor.execute(get_password_query, (email,))
            hashed_password_in_db = cursor.fetchone()

            if hashed_password_in_db and bcrypt.checkpw(password.encode('utf-8'), hashed_password_in_db[0].encode('utf-8')):
                return True
        except (Exception, psycopg2.Error) as error:
            print("Error while handling user login:", error)
        finally:
            conn.close()
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        conn = connect_to_db()

        if conn:
            if register_user(conn, username, first_name, last_name, email, password):
                return "Registration successful", 200  # Return a success response with HTTP status 200
            else:
                return "Registration failed", 400  # Return a failure response with HTTP status 400
        else:
            return "Database connection error", 500  # Return an error response if there's a database connection issue

    return "Invalid request method", 405  # Return an error response for other HTTP methods

# Handle other HTTP methods gracefully by returning an error response.

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if login_user(email, password):
            return "Login successful"
        else:
            return "Invalid login"

if __name__ == "__main__":
    app.run(debug=True)
