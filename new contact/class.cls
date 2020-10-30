// Apex Controller for Contact List Lightning Component
public class ContactListController {
        
    @AuraEnabled
    public static List<Contact> getContactList(List<Id> accountIds) {
        // Getting the list of contacts from where Id is in accountIds
                List<Contact> contactList = [SELECT Id, FirstName, LastName, Email, Phone, AccountId FROM Contact WHERE AccountId in :accountIds];
                // Returning the contact list
        return contactList;
    }

    @AuraEnabled
    public static Map<String,String> saveContactList(List<Contact> contactList) {
        // Forming a  string map to return response
        Map<String,String> resultMap = new Map<String,String>();
        // Adding try catch for exception handling
        try {
                // Updating the Contact List
            update contactList;
            // Setting the success status and message in resultMap
            resultMap.put('status', 'success');
                resultMap.put('message', 'Contacts Updated Successfully');        
        }
        catch(Exception e) {
            // Setting the error status and message in resultMap
            resultMap.put('status', 'error');
                        resultMap.put('message',e.getMessage());
        }
        // Returning the result string map
        return resultMap;
    }
    
    @AuraEnabled
    public static Map<String,String> deleteContactList(List<Id> contactIds) {
        //Fetching Contacts
        List<Contact> contactsToDelete = [SELECT Id FROM Contact WHERE Id in :contactIds];
        // Forming a  string map to return response
        Map<String,String> resultMap = new Map<String,String>();
        // Adding try catch for exception handling
        try {
                // Deleting the Contacts
            delete contactsToDelete;
            // Setting the success status and message in resultMap
            resultMap.put('status', 'success');
                resultMap.put('message', 'Contacts Deleted Successfully');        
        }
        catch(Exception e) {
            // Setting the error status and message in resultMap
            resultMap.put('status', 'error');
                        resultMap.put('message',e.getMessage());
        }
        // Returning the result string map
        return resultMap;                
    }

    @AuraEnabled
    public static Map<String, String> createContactRecord(Contact newContact) {
        // Forming a  string map to return response
        Map<String,String> resultMap = new Map<String,String>();
        // Adding try catch for exception handling
        try {
            // Inserting the Contact
            insert newContact;
            // Setting the success status and message in resultMap
            resultMap.put('status', 'success');
            resultMap.put('message', 'Contact Inserted Successfully');        
        }
        catch(Exception e) {
            // Setting the error status and message in resultMap
            resultMap.put('status', 'error');
            resultMap.put('message',e.getMessage());
        }
        // Returning the result string map
        return resultMap;        
    }
}