import subprocess
import json
import sys

# Cherwell REST API endpoint URL
api_url = "https://charter.cherwellondemand.com/CherwellAPI/token"

try:
    # Use curl to make the HTTP request and capture the output
    curl_command = f"curl -s '{api_url}'"
    api_response = subprocess.check_output(curl_command, shell=True)

    # Parse the JSON response using Python
    response_data = json.loads(api_response.decode('utf-8'))

    # Extract and print the access token
    access_token = response_data.get("access_token")
    if access_token:
        print('Access Token:', access_token)
    else:
        print('Error: "access_token" not found in the API response.')

except subprocess.CalledProcessError as e:
    print(f"Error executing curl command: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
except KeyError:
    print('Error: "access_token" key not found in the API response.')
except Exception as e:
    print(f"An unexpected error occurred: {e}")
