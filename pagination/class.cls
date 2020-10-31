public class PaginationForDataTable {
    //Get Account Records
    @AuraEnabled
    public static List<Account> getAccountsPage(String pageSize, String pageNumber){
        Integer psize = Integer.valueOf(pageSize);
        Integer pnumber = Integer.valueOf(pageNumber)-1;
         
        List<Account> accList = [SELECT Id, Name, AccountNumber, Industry, Phone
                                  FROM Account LIMIT :Integer.valueOf(psize) OFFSET :(psize*pnumber)];
        //return list of accounts
        return accList;
    }
}