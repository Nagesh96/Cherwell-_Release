from CherwellAPI import CherwellClient

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>, <api_key>, <username>, <password>)

# Create a new instance of a Release business object
release = cherwell_client.get_new_business_object("Release")

# Set the properties of the new Release using a dictionary
release_properties = {
    "Name": "New Release",
    "Description": "This is a test Release",
    "Status": "Draft",
    "ReleaseDate": "2023-12-31T00:00:00Z"
}
release.set_properties(release_properties)

# Save the new Release
release.Save()

# Show the new business object record id
print("RecId for new Release: {}".format(release.busObRecId))
print("PublicId for new Release: {}".format(release.busObPublicId))
