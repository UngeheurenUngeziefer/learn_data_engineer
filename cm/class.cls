public with sharing class AccountCtrl { 
    @AuraEnabled
    public static List<Contact> getContactData(){
        return [select Id,Name from Contact LIMIT 10];
	}
    
    @AuraEnabled
    public static List<Contact> deleteContact(String ContactId)
    {
        Contact delContact=[Select Id from Contact where id=:ContactId LIMIT 10];
        delete delContact;
        return getContactData();
    }
    
    @AuraEnabled
    public static List<Contact> getAccountsPage(String pageSize, String pageNumber){
        Integer psize = Integer.valueOf(pageSize);
        Integer pnumber = Integer.valueOf(pageNumber)-1;
         
        List<Contact> accList = [SELECT Id, Name, Email, Phone
                                  FROM Contact LIMIT :Integer.valueOf(psize) OFFSET :(psize*pnumber)];
        //return list of accounts
        return accList;
    }
}