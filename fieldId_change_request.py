import requests

# Cherwell API endpoints
token_url = "https://your-cherwell-instance/token"
business_object_schema_url = "https://your-cherwell-instance/api/V1/getbusinessobject/schema/{business_object_name}"

# Cherwell credentials
cherwell_username = "your_username"
cherwell_password = "your_password"
client_id = "your_client_id"
client_secret = "your_client_secret"
business_object_name = "Change Request"

# Request access token
token_payload = {
    "grant_type": "password",
    "username": cherwell_username,
    "password": cherwell_password,
    "client_id": client_id,
    "client_secret": client_secret,
}

token_response = requests.post(token_url, data=token_payload)

if token_response.status_code == 200:
    access_token = token_response.json().get("access_token")

    # Request business object schema with access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    business_object_schema_response = requests.get(business_object_schema_url.format(business_object_name), headers=headers)

    if business_object_schema_response.status_code == 200:
        data = business_object_schema_response.json()
        
        # Extract and print field IDs
        fields = data.get("fields", [])
        for field in fields:
            field_name = field.get("name")
            field_id = field.get("fieldId")
            print(f"Field: {field_name}, Field ID: {field_id}")
    else:
        print(f"Failed to retrieve business object schema. Status code: {business_object_schema_response.status_code}")
else:
    print(f"Failed to obtain access token. Status code: {token_response.status_code}")
