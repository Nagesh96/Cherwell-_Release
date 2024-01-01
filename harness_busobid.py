# Cherwell API details
baseUrl="https://charter.cherwellondemand.com"
CLIENT_ID="<+secrets.getValue("account.ARAClientPROD_Client_ID")>"
USERNAME="ARAClientPROD"
PASSWORD="<+secrets.getValue("account.ARAClientPROD")>"

# Get Authorization token
AUTH_TOKEN_RESPONSE=$(curl -s -X POST --header "Content-Type: application/x-www-form-urlencoded" --header "Accept: application/json" -d "grant_type=password&client_id=$CLIENT_ID&username=$USERNAME&password=$PASSWORD" "$baseUrl/CherwellAPI/token"| /apps/svc_smobusr/db_deployment/jq -r '.access_token')

echo "Current API Token:" $AUTH_TOKEN_RESPONSE

# Continue with the rest of the script...

# Business Object details
BUSINESS_OBJECT_NAME="ChangeRequest"

# Fetch busObId for the Change Request Business Object
BUSOBID=$(curl -s -X GET "$CHERWELL_URL/busobdefinition?busobname=$BUSINESS_OBJECT_NAME" -H "Authorization: $AUTH_TOKEN_RESPONSE" | /apps/svc_smobusr/db_deployment/jq -r '.busObId')

echo "busObId for $BUSINESS_OBJECT_NAME: $BUSOBID"





# Fetch busObId for the Change Request Business Object
BUSOBID_RESPONSE=$(curl -s -X GET "$baseUrl/busobdefinition?busobname=$BUSINESS_OBJECT_NAME" -H "Authorization: $AUTH_TOKEN_RESPONSE")

# Check for errors in the response
if [[ $(echo "$BUSOBID_RESPONSE" | /apps/svc_smobusr/db_deployment/jq -e .error) != "null" ]]; then
    echo "Error in busObId response:"
    echo "$BUSOBID_RESPONSE" | /apps/svc_smobusr/db_deployment/jq .
    exit 1
fi

# Extract the busObId from the response
BUSOBID=$(echo "$BUSOBID_RESPONSE" | /apps/svc_smobusr/db_deployment/jq -r '.busObId')

echo "busObId for $BUSINESS_OBJECT_NAME: $BUSOBID"




curl -s 'https://api.github.com/users/lambda' | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['name'])"
