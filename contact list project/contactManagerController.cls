@AuraEnabled
public static List<Opportunity> fetchOpportunity(string searchKeyWord) {
    List<Opportunity> returnList = new List<Opportunity>();
    
    String searchKey = String.isBlank(searchKeyWord) ? '%%' : searchKeyWord + '%';
    
    returnList = [SELECT Id
                  	   , Name
                  	   , Account_Name__c
                  	   , CloseDate
                       , Amount
                    FROM Opportunity
                   WHERE Name
                  	LIKE :searchKey
                   LIMIT 15];
    
    
    return returnList;

}