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



baseUrl="https://charter.cherwellondemand.com"
AUTH_TOKEN_RESPONSE=$(curl -s -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" -d "grant_type=password&client_id=<+secrets.getValue("account.ARAClientPROD_Client_ID")>&username=ARAClientPROD&password=<+secrets.getValue("account.ARAClientPROD")>" "$baseUrl/CherwellAPI/token"| /apps/svc_smobusr/db_deployment/jq -r '.access_token')
#token=$(echo -n "$AUTH_TOKEN_RESPONSE" | /apps/svc_smobusr/db_deployment/jq -sr '.["access_token"]')
echo "Current API Token:" $AUTH_TOKEN_RESPONSE
