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

    # Prepare the request payload for the release ticket
    release_payload = {
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

    # Convert release payload to JSON
    release_json_payload = json.dumps(release_payload)

    # Make the API request to create the release ticket
    release_response = requests.post(f'{cherwell_url}/api/V1/your_release_api_endpoint', data=release_json_payload, headers=headers)

    # Check if the release request was successful
    if release_response.status_code == 201:
        # Parse the release response JSON
        release_json = release_response.json()

        # Extract public ID and record ID of the release ticket
        release_public_id = release_json.get('businessObject').get('publicId')
        release_record_id = release_json.get('businessObject').get('recordId')

        print(f'Release Ticket created successfully. Public ID: {release_public_id}, Record ID: {release_record_id}')

        # Prepare the request payload for the change request
        change_payload = {
            'businessObject': {
                'ChangeTitle': 'Related Change Request',
                'Description': 'Description of the related change request',
                'AssignedGroup': 'Change Management',
                'RelatedRelease': {
                    'Link': f'your_cherwell_url/your_release_api_endpoint/{release_record_id}'
                }
                # Add more fields as needed
            }
        }

        # Convert change payload to JSON
        change_json_payload = json.dumps(change_payload)

        # Make the API request to create the change request ticket
        change_response = requests.post(f'{cherwell_url}/api/V1/your_change_api_endpoint', data=change_json_payload, headers=headers)

        # Check if the change request was successful
        if change_response.status_code == 201:
            # Parse the change response JSON
            change_json = change_response.json()

            # Extract public ID and record ID of the change request ticket
            change_public_id = change_json.get('businessObject').get('publicId')
            change_record_id = change_json.get('businessObject').get('recordId')

            print(f'Change Request Ticket created successfully. Public ID: {change_public_id}, Record ID: {change_record_id}')
        else:
            print(f'Error creating Change Request Ticket. Status code: {change_response.status_code}, Response: {change_response.text}')
    else:
        print(f'Error creating Release Ticket. Status code: {release_response.status_code}, Response: {release_response.text}')

# Call the function to create a Cherwell release ticket and a related change request ticket
create_cherwell_ticket()
