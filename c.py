using System.Collections.Generic;
using System.Linq;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace Trebuchet.WebApi.IntegrationTests.ExamplesForCustomers.Create_an_Object
{
    public class CreateAnObject
    {
        public void CreateAnIncident()
        {
            //Get an access token using CSM credentials
            var serviceApi = new ServiceApi("http://your server/CherwellApi/");
            var tokenResponse = serviceApi.ServiceToken("password",
                "your client id", null, "CSDAdmin", "CSDAdmin", null,
                "Internal");

            //Create a new Business Object api object and add the default header
            var businessObjectApi = new BusinessObjectApi("http://your server/CherwellApi/");
            businessObjectApi.Configuration.AddDefaultHeader("Authorization",
                "Bearer " + tokenResponse.AccessToken);

            //Create a new Searches api object and add the default header
            var searchesApi = new SearchesApi("http://your server/CherwellApi");
            searchesApi.Configuration.AddDefaultHeader("Authorization",
                "Bearer " + tokenResponse.AccessToken);

            //Get the Business Object summary for customer internal
            var businessObjectSummaryCustomerInternal =
                businessObjectApi.BusinessObjectGetBusinessObjectSummaryByNameV1("CustomerInternal");

            //Get the Business Object schema for customer internal
            var schemaResponse =
                businessObjectApi.BusinessObjectGetBusinessObjectSchemaV1(
                    businessObjectSummaryCustomerInternal[0].BusObId, false);

            //Create the Search results request to lookup the customer and get the customers record ID
            var searchResultsRequest = new SearchResultsRequest();
            searchResultsRequest.BusObId = businessObjectSummaryCustomerInternal[0].BusObId;
            searchResultsRequest.Filters = new List<FilterInfo>();
            var filterInfo = new FilterInfo();
            filterInfo.FieldId =
                schemaResponse.FieldDefinitions.First(f => f.Name == "FullName").FieldId;
            filterInfo.Operator = "eq";
            filterInfo.Value = "Eric Cox";
            searchResultsRequest.Filters.Add(filterInfo);

            //Run the Search 
            var searchResultsResponse =
                searchesApi.SearchesGetSearchResultsAdHocV1(searchResultsRequest);

            //Set the record ID to be used in the creation of the Incident
            var customerRecId = searchResultsResponse.BusinessObjects[0].BusObRecId;


            //Get the field template for Incident to help set the fields
            var templateRequest = new TemplateRequest();

            //Get the Business Object summary for Incident
            var businessObjectSummaryIncident =
                businessObjectApi.BusinessObjectGetBusinessObjectSummaryByNameV1("Incident");

            templateRequest.BusObId = businessObjectSummaryIncident[0].BusObId;
            templateRequest.IncludeAll = true;

            //Use the template to set the fields
            var templateResponse =
                businessObjectApi.BusinessObjectGetBusinessObjectTemplateV1(templateRequest);

            SetFieldValue(templateResponse.Fields, "Status", "New");
            SetFieldValue(templateResponse.Fields, "Description", "New Incident");
            SetFieldValue(templateResponse.Fields, "ShortDescription", "Short Description");
            SetFieldValue(templateResponse.Fields, "CustomerRecID", customerRecId);
            SetFieldValue(templateResponse.Fields, "Priority", "2");
            SetFieldValue(templateResponse.Fields, "Source", "Phone");
            SetFieldValue(templateResponse.Fields, "IncidentType", "Incident");
            SetFieldValue(templateResponse.Fields, "Service", "Employee Support");
            SetFieldValue(templateResponse.Fields, "Category", "Add/Change");
            SetFieldValue(templateResponse.Fields, "Subcategory", "New Employee Setup");

            //Create the save request
            var saveRequest = new SaveRequest();
            saveRequest.BusObId = businessObjectSummaryIncident[0].BusObId;
            saveRequest.Fields = templateResponse.Fields;

            //Create the Incident
            var saveResponse = businessObjectApi.BusinessObjectSaveBusinessObjectV1(saveRequest);
        }

        public void SetFieldValue(List<FieldTemplateItem> fields, string fieldName,
            string fieldValue)
        {
            var fieldTemplate = fields.First(s => s.Name.Equals(fieldName));
            if (fieldTemplate != null)
            {
                fieldTemplate.Value = fieldValue;
                fieldTemplate.Dirty = true;
            }
        }
    }
}
