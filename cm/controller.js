({
    // this function call on the component load first time 
    doInit : function(component, event, helper){
        // call the helper function         
        helper.getColumn(component);
        helper.getAccountsPage(component, helper);
        
    },
    // this function call on click on the next page button 
    handleNext : function(component, event, helper) { 
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber+1);
        helper.getAccountsPage(component, helper);
    },
    // this function call on click on the previous page button  
    handlePrev : function(component, event, helper) {        
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber-1);
        helper.getAccountsPage(component, helper);
    },
    
    searchTable : function(cmp,event,helper) {
        var allRecords = cmp.get("v.data");
        var searchFilter = event.getSource().get("v.value").toUpperCase();
        var blankSearch = '';   
        
        var tempArray = [];
        var i;

        
        for(i=0; i < allRecords.length; i++){
            if((allRecords[i].Name && allRecords[i].Name.toUpperCase().indexOf(searchFilter) != -1))
            {
                tempArray.push(allRecords[i]);
            }
        }
                
        cmp.set("v.data",tempArray);
        
        },
        
        
    
    fetchAccounts : function(component, event, helper) {
        component.set('v.columns', [
            {label: 'Name', fieldName: 'Name', type: 'text', sortable: true},
            {label: 'Email', fieldName: 'Email', type: 'Email', sortable: true},
            {label: 'Phone', fieldName: 'Phone', type: 'phone', sortable: true},		
            {label: 'Delete Contact', type:  'button', typeAttributes: { iconName: 'utility:delete',  label: 'Del', name: 'deleteRecord', 
                                               title: 'deleteTitle', disabled: false, value: 'test'}}
        ]);
        var action = component.get("c.fetchAccts");
        action.setParams({
        });
        action.setCallback(this, function(response){
            var state = response.getState();
            if (state === "SUCCESS") {
                component.set("v.data", response.getReturnValue());
                helper.sortData(component, component.get("v.sortedBy"), component.get("v.sortedDirection"));
            }
        });
        $A.enqueueAction(action);
    },
    
    updateColumnSorting: function (cmp, event, helper) {
        var fieldName = event.getParam('fieldName');
        var sortDirection = event.getParam('sortDirection');
        cmp.set("v.sortedBy", fieldName);
        cmp.set("v.sortedDirection", sortDirection);
        helper.sortData(cmp, fieldName, sortDirection);
    },
            
    createRecord : function (component, event, helper) {
            var createRecordEvent = $A.get("e.force:createRecord");
            createRecordEvent.setParams({
                "entityApiName": "Contact"
            });
            createRecordEvent.fire();
    },
    
    deleteRecord : function(component, event, helper) {
        var selectedItem = event.currentTarget;
        var recId = selectedItem.dataset.record;
        alert(recId); // this is correctly showing the right Salesforce Id
        var action = component.get("c.delRecord");
        action.setParams({
            "recId" : recId
        });
        $A.enqueueAction(action);
        window.location.reload();
    }
	
            
})