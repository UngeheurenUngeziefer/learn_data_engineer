@isTest
	public class Test_ContactTrigger {
      
    // добавление контакта
    @isTest static void testAddContact() {
        Contact testContact = new Contact(
            LastName = 'LastNameWithout',
            Email = 'e@ma.il'
        );
        Integer lengthBefore = [SELECT Id FROM Contact].size();
        insert testContact;
        
              
        Integer lengthAfter = [SELECT Id FROM Contact].size();
        System.assertNotEquals(lengthBefore, lengthAfter, 'Контакт не добавлен');
    }
    
    // удаление контакта
    @isTest static void testDeleteContact() {
        Contact testContact = new Contact(
            LastName = 'LastNameWithout',
            Email = 'e@ma.il'
        );
        insert testContact;
        
        Integer lengthBefore = [SELECT Id FROM Contact].size();
        
        delete testContact;
        Integer lengthAfter = [SELECT Id FROM Contact].size();
        System.assertNotEquals(lengthBefore, lengthAfter, 'Контакт не удалён');
    }
     
    // working статус
    @isTest static void workingStatus() {
    	Contact testContact = new Contact(
            LastName = 'LastNameWithout',
            Email = 'e@ma.il'
        );
        
        insert testContact;
        Case cs = new Case();
        cs.Status = 'Working';
        cs.Origin = 'New Contact';
        
     	System.assertEquals(cs.Status, 'Working', 'Не равно working');   
        
    }
    
    // ownerId
    @isTest static void ownerId() {
    	Contact testContact = new Contact(
            LastName = 'LastNameWithout',
            Email = 'e@ma.il'
        );
        
        insert testContact;
        Case cs = new Case();
     	System.assertEquals(cs.OwnerId, testContact.AccountId, 'OwnerId не равны');   
        
    }
        
      // сравнение аккаунт id
    @isTest static void caseCreating() {
        Integer lengthBefore = [SELECT Id FROM Case].size();
        Account testAccount = new Account(
            Name = 'AccountName'
        );
        insert testAccount;
        
        Contact testContact = new Contact(
            LastName = 'LastName',
            Email = 'e@ma.il',
            AccountId = testAccount.Id
        );
        insert testContact;
        
        Integer lengthAfter = [SELECT Id FROM Case].size();
        System.assertNotEquals(lengthBefore, lengthAfter, 'Case не создаётся');
        System.assertEquals(testAccount.Id, testContact.AccountId, 'AccountId не совпадают');
        
	}
        
     // Заполнение полей 
     @isTest static void fieldsFilling() {
         Integer lengthBefore = [SELECT Id FROM Case].size();         
         
         Contact cn = new Contact(
         	LastName = 'LastName',
            Email = 'e@ma.il',
            Contact_Level__c = 'Primary'
         );
         insert cn;
         
         Contact cn2 = new Contact(
         	LastName = 'LastName2',
            Email = 'e2@ma.il',
            Contact_Level__c = 'Secondary'
         );
         insert cn2;
         
         Case cs = [SELECT ContactId FROM Case WHERE Priority =: 'High'];
         Case cs2 = [SELECT ContactId FROM Case WHERE Priority =: 'Medium'];
		 
         System.assertEquals(cs.ContactId, cn.AccountId, 'High');
         System.assertEquals(cs2.ContactId, cn2.AccountId, 'Medium');
     }
     	
        
          
     }