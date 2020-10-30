({
    // Function to fetch data from server called in initial loading of page
        fetchContacts : function(component, event, helper) {
        // Assign server method to action variable
        var action = component.get("c.getContactList");
        // Getting the account id from page
        var accountId = component.get("v.recordId");
        // Setting parameters for server method
        action.setParams({
            accountIds: accountId
        });
        // Callback function to get the response
        action.setCallback(this, function(response) {
            // Getting the response state
            var state = response.getState();
            // Check if response state is success
            if(state === 'SUCCESS') {
                // Getting the list of contacts from response and storing in js variable
                var contactList = response.getReturnValue();
                // Set the list attribute in component with the value returned by function
                component.set("v.contactList",contactList);
            }
            else {
                // Show an alert if the state is incomplete or error
                alert('Error in getting data');
            }
        });
        // Adding the action variable to the global action queue
        $A.enqueueAction(action);
        },
    
        readData : function(cmp) {
            // переменной recordID присваивается атрибут компонента
            // переменной action присваевается функция contacts в классе
            var recordId =  cmp.get("v.recordId");
            var action = cmp.get("c.contacts");
            // функции передаётся recordId
            action.setParams({ "currentRecordId" : recordId });
            action.setCallback(this, $A.getCallback(function (response) {
                var state = response.getState();
                var res = [];
                // сценарий возврата значений из таблицы
                if (state === "SUCCESS") {
                    var resp = response.getReturnValue();
                    console.log(resp);
                    resp.forEach(function(item, index, array) {                
                        let ob = {};
                        ob.Name = item.Contact.Name;
                        ob.Email = item.Email;
                        ob.ContactLevel = item.ContactLevel;
                        ob.Account = item.Opportunity.Account;
                        ob.Owner = item.Owner;
                        ob.CreatedBy = item.CreatedBy;
                        ob.CreatedDate = item.CreatedDate;
                        res.push(ob);
                    });
                    cmp.set('v.data', res);
                // сценарий ошибки
                } else if (state === "ERROR") {
                    var errors = response.getError();
                    console.error(errors);
                }
            }));
            $A.enqueueAction(action);
        },
    
})