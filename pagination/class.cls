public class SampleController {
     
    //Get Account Records
    @AuraEnabled
    public static List<Account> getAccounts(String pageSize, String pageNumber){
        List<Account> accList = new List<Account>();
        ApexPages.StandardSetController ssc = new ApexPages.StandardSetController(Database.getQueryLocator('SELECT Id, Name, AccountNumber, Industry, Phone FROM Account'));
        ssc.setpagesize(Integer.valueOf(pageSize));
        ssc.setPageNumber(Integer.valueOf(pageNumber));
        accList = (List<Account>)ssc.getRecords();
        return accList;
    }
     
    //Delete Account
    @AuraEnabled
    public static void deleteAccount(Account acc){
        Delete acc;
    } 
}