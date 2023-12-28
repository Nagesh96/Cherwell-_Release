import requests
import json

# Set the Cherwell API endpoint
api_url = "https://<your_cherwell_instance>/CherwellAPI/api/V1/savebusinessobject"

# Set the Cherwell API credentials
username = "<your_cherwell_username>"
password = "<your_cherwell_password>"
client_id = "<your_cherwell_client_id>"
client_secret = "<your_cherwell_client_secret>"

# Get the Cherwell API access token
auth_url = "https://<your_cherwell_instance>/CherwellAPI/token"
auth_data = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password
}
auth_response = requests.post(auth_url, data=auth_data)
access_token = auth_response.json()["access_token"]

# Set the Cherwell business object properties
business_object = {
    "busObId": "<your_release_ticket_busobid>",
    "fields": [
        {
            "dirty": True,
            "name": "<your_release_ticket_fieldname_1>",
            "value": "<your_release_ticket_fieldvalue_1>"
        },
        {
            "dirty": True,
            "name": "<your_release_ticket_fieldname_2>",
            "value": "<your_release_ticket_fieldvalue_2>"
        },
        {
            "dirty": True,
            "name": "<your_release_ticket_fieldname_3>",
            "value": "<your_release_ticket_fieldvalue_3>"
        }
    ]
}

# Set the Cherwell API headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + access_token
}

# Create the new release ticket
response = requests.post(api_url, headers=headers, data=json.dumps(business_object))

# Check the response status code
if response.status_code == 200:
    print("New release ticket created successfully!")
    # Get the busObPublicId and busObRecId of the new release ticket
    response_json = response.json()
    busObPublicId = response_json["busObPublicId"]
    busObRecId = response_json["busObRecId"]
    print("busObPublicId: {}".format(busObPublicId))
    print("busObRecId: {}".format(busObRecId))
else:
    print("Failed to create new release ticket.")
