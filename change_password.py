import requests
import getpass  # Import the getpass library for securely inputting passwords

# Define the API endpoint URL
url = 'http://localhost:5000/change_password'

# User data to be sent in JSON format
user_data = {
    'username': 'alvin',  # Replace with the username you want to change the password for
    'current_password': '',  # Leave this empty to securely input the current password
    'new_password': '',  # Leave this empty to securely input the new password
}

# Securely input the current password and new password
user_data['current_password'] = getpass.getpass(prompt='Enter current password: ')
user_data['new_password'] = getpass.getpass(prompt='Enter new password: ')

# Send a POST request to change the user's password
response = requests.post(url, json=user_data)

# Check the response
if response.status_code == 200:
    print("Password changed successfully")
else:
    print("Failed to change password")
    print(response.status_code, response.text)
