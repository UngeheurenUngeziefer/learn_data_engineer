({
    onInit : function(component,event,helper){
        // Setting column information.To make a column sortable,set sortable as true on component load
        component.set("v.contactColumns",[
            { label : 'Name', fieldName : 'Name', type : 'Name', sortable : true },
            { label : 'Phone', fieldName : 'Phone', type : 'Phone', sortable : true },
            { label : 'Contact Level', fieldName : 'Contact_Level__c', type : 'Picklist', sortable : true },
            { label : 'Account', fieldName : 'Account', type : 'Lookup', sortable : true },
            { label : 'Owner', fieldName : 'OwnerId', type : 'lookup', sortable : true },
            { label : 'Created By', fieldName : 'CreatedById', type : 'Lookup(User)', sortable : true },
            { label : 'Created Date', fieldName : 'CreatedDate', type : 'Date/Time', sortable : true },
        ]);
        var action = component.get("c.fetchData");
        action.setCallback(this, function(response){
            var state = response.getState();
            if (state === "SUCCESS") {
                component.set("v.contactData", response.getReturnValue());
                component.set("v.filteredData", response.getReturnValue());
            }
        });
        $A.enqueueAction(action);
        // call helper function to fetch account data from apex
        helper.getAccountData(component);
    },
    
    //Method gets called by onsort action,
    handleSort : function(component,event,helper){
        //Returns the field which has to be sorted
        var sortBy = event.getParam("fieldName");
        //returns the direction of sorting like asc or desc
        var sortDirection = event.getParam("sortDirection");
        //Set the sortBy and SortDirection attributessadsad
        component.set("v.sortBy",sortBy);
        component.set("v.sortDirection",sortDirection);
        // call sortData helper function
        helper.sortData(component,sortBy,sortDirection);
    },
            
   	searchTable : function(cmp,event,helper) {
        var allRecords = cmp.get("v.contactData");
        var searchFilter = event.getSource().get("v.value").toUpperCase();
        
        var tempArray = [];
        var i;

        for(i=0; i < allRecords.length; i++){
            if((allRecords[i].Name && allRecords[i].Name.toUpperCase().indexOf(searchFilter) != -1))
            {
                tempArray.push(allRecords[i]);
            }
        }
        cmp.set("v.filteredData",tempArray);
    }
})