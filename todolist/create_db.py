from app import app, db  # Import your Flask app and SQLAlchemy db
import MySQLdb

# Database configuration
db_username = 'root'
db_password = 'password123'  # Replace with your MySQL root password
db_host = 'localhost'
db_name = 'students'

# Connect to MySQL without specifying a database
connection = MySQLdb.connect(
    host=db_host,
    user=db_username,
    password=db_password
)

cursor = connection.cursor()

# Check if the database exists
cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
result = cursor.fetchone()

if not result:
    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"Database '{db_name}' created successfully.")
else:
    print(f"Database '{db_name}' already exists.")

cursor.close()
connection.close()

# Update the SQLALCHEMY_DATABASE_URI to include the database name
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'

# Proceed to create tables within the database
with app.app_context():
    db.create_all()
    print("Tables created successfully.")
