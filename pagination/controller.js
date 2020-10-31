({
    // this function call on the component load first time 
    doInit : function(component, event, helper){
        // call the helper function         
        helper.getColumn(component);
        helper.getAccounts(component, helper);
    },
    // this function call on click on the next page button 
    handleNext : function(component, event, helper) { 
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber+1);
        helper.getAccounts(component, helper);
    },
    // this function call on click on the previous page button  
    handlePrev : function(component, event, helper) {        
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber-1);
        helper.getAccounts(component, helper);
    },
})