({
	myAction : function(component, event, helper) {
		var action =component.get("c.getAllAccounts");
        console.log('The action value is: '+action);
         action.setCallback(this, function(a){ 
             
            component.set("v.accounts", a.getReturnValue());
           //  console.log('The accs are :'+JSON.stringify(a.getReturnValue()));
            console.log('The accs are :'+JSON.stringify(a.getReturnValue()));
          
        });
        $A.enqueueAction(action);
	},
    
    // Function called on initial page loading to get contact list from server
        getContactsList : function(component, event, helper) {
        // Helper function - fetchContacts called for interaction with server
                helper.fetchContacts(component, event, helper);
        },

    // Function used to create a new Contact
    newContact: function(component, event, helper) {
        // Global event force:createRecord is used
        var createContact = $A.get("e.force:createRecord");
        // Parameters like apiName and defaultValues are set
        createContact.setParams({
            "entityApiName": "Contact",
            "defaultFieldValues": {
                "AccountId": component.get("v.recordId")
            }
        });
        // Event fired and new contact dialog open
        createContact.fire();
    }
})
