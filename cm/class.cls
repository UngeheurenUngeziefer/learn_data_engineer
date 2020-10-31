public class PaginationForDataTable {
    //Get Account Records dfs
    @AuraEnabled
    public static List<Contact> getAccountsPage(String pageSize, String pageNumber){
        Integer psize = Integer.valueOf(pageSize);
        Integer pnumber = Integer.valueOf(pageNumber)-1;
         
        List<Contact> accList = [SELECT Id, Name, Email, Phone
                                  FROM Contact LIMIT :Integer.valueOf(psize) OFFSET :(psize*pnumber)];
        //return list of accounts
        return accList;
    }
    
    @AuraEnabled
    public static List <Contact> fetchAccts() {
        return [SELECT Id, Name, Email, Phone
				FROM Contact LIMIT 10];
    }
 
}





    
