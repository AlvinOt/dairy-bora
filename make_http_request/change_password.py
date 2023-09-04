import requests
import bcrypt

# Define the API endpoint URL
url = 'http://localhost:5000/change_password'

# User data to be sent in JSON format
user_data = {
    'username': 'jondoe',
    'current_password': 'doepword!123',  # Provide the current password
    'new_password': 'pwordjdoe!23'  # Provide the new password
}

# Send a POST request to change the user's password
response = requests.post(url, json=user_data)

# Check the response
if response.status_code == 200:
    print("Password changed successfully")
else:
    print("Failed to change password")
    print(response.status_code, response.text)
