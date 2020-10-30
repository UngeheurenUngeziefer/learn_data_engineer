public class MyOpportunityListController {

    @AuraEnabled
    public static List<Opportunity> fetchOpportunity(String searchKeyWord) {
        List<Opportunity> returnList = new List<Opportunity>();

        String searchKey = String.isBlank(searchKeyWord) ? '&&' : searchKeyWord + '&';

        returnList = [SELECT Id
                           , Name
                           , CloseDate
                           , Amount
                        FROM Opportunity
                        WHERE Name
                        LIKE :searchKey
                        LIMIT 15];
        return returnList;
    }
}