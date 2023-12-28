import requests
import json

def create_cherwell_tickets():
    cherwell_url = 'your_cherwell_url'
    api_key = 'your_api_key'

    # Prepare the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Apikey {api_key}'
    }

    # Create the release ticket
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

    release_json_payload = json.dumps(release_payload)

    release_response = requests.post(f'{cherwell_url}/api/V1/your_release_api_endpoint', data=release_json_payload, headers=headers)

    if release_response.status_code == 201:
        release_json = release_response.json()
        release_record_id = release_json.get('businessObject').get('recordId')
        print(f'Release Ticket created successfully. Record ID: {release_record_id}')

        # Create the change request
        change_payload = {
            'businessObject': {
                'ChangeTitle': 'New Change Request',
                'Description': 'Description of the new change request',
                'AssignedGroup': 'Change Management'
                # Add more fields as needed
            }
        }

        change_json_payload = json.dumps(change_payload)

        change_response = requests.post(f'{cherwell_url}/api/V1/your_change_api_endpoint', data=change_json_payload, headers=headers)

        if change_response.status_code == 201:
            change_json = change_response.json()
            change_record_id = change_json.get('businessObject').get('recordId')
            print(f'Change Request created successfully. Record ID: {change_record_id}')

            # Link the change request to the release ticket
            link_payload = {
                'relatedItems': [
                    {
                        'action': 'Link',
                        'type': 'ChangeRequest',
                        'id': change_record_id
                    }
                ]
            }

            link_json_payload = json.dumps(link_payload)

            link_response = requests.post(f'{cherwell_url}/api/V1/your_link_api_endpoint/{release_record_id}', data=link_json_payload, headers=headers)

            if link_response.status_code == 200:
                print('Change Request linked successfully.')
            else:
                print(f'Error linking Change Request. Status code: {link_response.status_code}, Response: {link_response.text}')
        else:
            print(f'Error creating Change Request. Status code: {change_response.status_code}, Response: {change_response.text}')
    else:
        print(f'Error creating Release Ticket. Status code: {release_response.status_code}, Response: {release_response.text}')

# Call the function to create a Cherwell release ticket, a new change request, and link them
create_cherwell_tickets()￼Enter
