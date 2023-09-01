import requests
import bcrypt

# Define the API endpoint URL
url = 'http://localhost:5000/add_users'

# User data to be sent in JSON format
user_data = {
    'username': 'jontedoe',
    'password_hashed': 'doughpword!123',  # Replace with the actual hashed password
    'role': 'marketingmanager',
    'contact_information': 'doe@mail.com'
}

# Send a POST request to create the user
response = requests.post(url, json=user_data)

# Check the response
if response.status_code == 201:
    print("User created successfully")
else:
    print("Failed to create user")
    print(response.status_code, response.text)

