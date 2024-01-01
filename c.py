import requests
import json
import sys
# Cherwell REST API endpoint URL
url = "https://charter.cherwellondemand.com/CherwellAPI/token"

# client credentials
username = sys.argv[1]
print('UserName: ',username)
password = sys.argv[2]
print('Password: ',password)
client_id = sys.argv[3]
print('Client ID:',client_id)
grant_type = "password"

# request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

# request body
data = {
    "username": username,
    "password": password,
    "client_id": client_id,
    "grant_type": grant_type
}

# Send the POST request to the Cherwell authentication server
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# Extract the access token from the JSON response
access_token = response.json()["access_token"]
print('Access Token: ',access_token)
