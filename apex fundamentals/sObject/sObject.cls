// sObj created
sObject s = new Invoice_Statement__c();
// field name,             new sObj                  fields determined
Invoice_Statement__c inv = new Invoice_Statement__c(Description__c='Test Invoice',
Status__c='Pending');
// sObj cast to mySObjectVar
Invoice_Statement__c inv = (Invoice_Statement__c)mySObjectVar;
// desc field setted as Test Invoice
inv.Description__c = 'Test Invoice';
// dot notation to read field values
ID id = inv.Id;
String x = inv.Name;

Invoice_Statement__c inv = new Invoice_Statement__c();
inv.Description__c = 'Large invoice';
System.debug('Invoice Description: ' + inv.Description__c);

sObjectTypeName parentObject = objectA.RelationshipName;
DataType s = objectA.RelationshipName.FieldName;
List<sObjectTypeName> children = objectA.ChildRelationshipName;

SELECT RelationshipName.Field FROM sObjectName WHERE Where_Condition [...]
SELECT field1, field1, ..., (Nested query for child sObjects)
FROM sObjectName WHERE Where_Condition [...]

Line_Item__c li = [SELECT Invoice_Statement__r.Name FROM Line_Item__c LIMIT 1];
// Traverses a relationship using the dot notation.
System.debug('Invoice statement name: ' + li.Invoice_Statement__r.Name);

