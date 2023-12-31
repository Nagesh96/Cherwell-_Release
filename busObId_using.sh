#!/bin/bash

# Cherwell API details
CHERWELL_URL="<Cherwell_URL>/api/V1"
CLIENT_ID="<Your_Client_ID>"
USERNAME="<Your_Username>"
PASSWORD="<Your_Password>"

# Get Authorization token
TOKEN=$(curl -s -X POST "$CHERWELL_URL/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=password&client_id=$CLIENT_ID&username=$USERNAME&password=$PASSWORD" | jq -r '.access_token')

# Business Object details
BUSINESS_OBJECT_NAME="ChangeRequest"

# Fetch busObId for the Change Request Business Object
BUSOBID=$(curl -s -X GET "$CHERWELL_URL/busobdefinition?busobname=$BUSINESS_OBJECT_NAME" -H "Authorization: $TOKEN" | jq -r '.busObId')

echo "busObId for $BUSINESS_OBJECT_NAME: $BUSOBID"
