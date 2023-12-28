import requests
import json

def create_cherwell_ticket():
    cherwell_url = 'your_cherwell_url'
    api_key = 'your_api_key'

    # Prepare the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Apikey {api_key}'
    }

    # Prepare the request payload
    payload = {
        'businessObject': {
            'ReleaseTitle': 'New Release',
            'Description': 'Description of the new release',
            'AssignedGroup': 'Support',
            'Requester': {
                'Name': 'John Doe',
                'Email': 'john.doe@example.com'
            }
            # Add more fields as needed
        }
    }

    # Convert payload to JSON
    json_payload = json.dumps(payload)

    # Make the API request to create the ticket
    response = requests.post(f'{cherwell_url}/api/V1/your_api_endpoint', data=json_payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 201:
        print('Ticket created successfully.')
    else:
        print(f'Error creating ticket. Status code: {response.status_code}, Response: {response.text}')

# Call the function to create a Cherwell ticket
create_cherwell_ticket()
