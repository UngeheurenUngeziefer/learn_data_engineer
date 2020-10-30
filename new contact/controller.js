public class SortableAccountTableController {
    // wrapper class 
     public class AccountWrapper{
         @AuraEnabled
         public String message;
         @AuraEnabled
         public List<Contact> contactList;
         @AuraEnabled
         public Boolean success;
     }
     
     //Return account records and message to be displayed in toast
     @AuraEnabled
     public static AccountWrapper getAccounts(){
         AccountWrapper accountWrapper = new AccountWrapper();
         try{
             accountWrapper.contactList = [SELECT ID, Name, Phone, Contact_Level__c, AccountId, OwnerId, CreatedById, CreatedDate
                                            FROM Contact
                                            LIMIT 50];
             accountWrapper.message = 'Account records are retrieved ';
             accountWrapper.success = true;
         }
         catch(Exception e){
             accountWrapper.message = e.getMessage();
             accountWrapper.success = false;
         }
         return accountWrapper;
     }
     
     @AuraEnabled
     public static List<sObject> fetchData() {
         //Query and return list of Contacts
         List<SObject> objRecords = [SELECT Name, Phone, Contact_Level__c, AccountId, OwnerId, CreatedById, CreatedDate from Contact LIMIT 20];
         return objRecords;
     }
 }