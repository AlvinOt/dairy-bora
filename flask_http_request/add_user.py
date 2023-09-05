import requests
import bcrypt  # Import the bcrypt library

# Define the API endpoint URL
url = 'http://localhost:5000/add_users'  # Use '/users' instead of '/add_users'

# Hash the password using bcrypt
password = 'hash123!password'  # Replace with the plain-text password you want to hash
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# User data to be sent in JSON format
user_data = {
    'username': 'cassim',
    'password_hashed': hashed_password,  # Use the hashed password
    'role': 'Farm Ownwer',
    'contact_information': 'cassim.com'
}

# Send a POST request to create the user
response = requests.post(url, json=user_data)

# Check the response
if response.status_code == 201:
    print("User created successfully")
else:
    print("Failed to create user")
    print(response.status_code, response.text)

