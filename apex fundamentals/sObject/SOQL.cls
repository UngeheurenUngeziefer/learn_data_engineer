//SOQL
sObject s = [SELECT Id, Name FROM Merchandise__c WHERE Name='Pencils'];

String myName = 'Pencils';
Merchandise__c[] ms = [SELECT Id FROM Merchandise__c WHERE Name=:myName];

// SOSL
List<List<SObject>> searchList = [FIND 'Pencil*' IN ALL FIELDS RETURNING
Merchandise__c (Id, Name), Invoice_Statement__c];
Merchandise__c[] merList = ((List<Merchandise__c>)searchList[0]);
Invoice_Statement__c[] invList = ((List<Invoice_Statement__c>)searchList[1]);
System.debug('Found ' + merList.size() + ' merchandise items.');
System.debug('Found ' + invList.size() + ' invoice statements.');