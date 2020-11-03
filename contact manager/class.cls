public with sharing class AccountCtrl { 
    
   @AuraEnabled
    public static List<Contact> getContactData()
    {
        return [SELECT Id, Name, Email, Contact_Level__c, AccountId, OwnerId, CreatedById, Birthdate 
                FROM Contact LIMIT 10];
	}
    
    @AuraEnabled
    public static List<Contact> deleteContact(String ContactId)
    {
        Contact delContact=[SELECT Id FROM Contact WHERE id=:ContactId LIMIT 10];
        delete delContact;
        return getContactData();
    }
    
    @AuraEnabled
    public static List<Contact> getAccountsPage(String pageSize, String pageNumber){
        Integer psize = Integer.valueOf(pageSize);
        Integer pnumber = Integer.valueOf(pageNumber)-1;
         
        List<Contact> accList = [SELECT Id, Name, Email, Contact_Level__c, AccountId, OwnerId, CreatedById, Birthdate
                                  FROM Contact LIMIT :Integer.valueOf(psize) OFFSET :(psize*pnumber)];
        //return list of accounts
        return accList;
    }
}