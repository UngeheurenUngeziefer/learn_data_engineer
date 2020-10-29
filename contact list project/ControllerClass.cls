public class accountsWithContactsClass {

@auraEnabled
public static list<Contact> getAllAccounts()
    {
       list<Contact> accs =[SELECT Id, Name, Email, Phone, AccountId FROM Contact];
      //  list<account> accs =[select id,name,phone,industry from account limit 10];
     //   return [select Id,Name from account limit 10];
     return accs;
    }
    
@AuraEnabled
public static List<Contact> getContactList(List<Id> accountIds) {
        // Getting the list of contacts from where Id is in accountIds
                List<Contact> contactList = [SELECT Id, Name, Email, Phone, AccountId FROM Contact WHERE AccountId in :accountIds];
                // Returning the contact list
        return contactList;
    }
    
    
    
}