({
    getColumn : function(component) {        
        component.set('v.columns', [
            {label: 'Name', fieldName: 'Name', type: 'text'},
            {label: 'Email', fieldName: 'Email', type: 'Email'},
            {label: 'Field', fieldName: 'Field', type: 'text'},
            {label: 'Phone', fieldName: 'Phone', type: 'phone'}           
        ]);
    },
     
    getAccountsPage : function(component, helper) {
        var action = component.get("c.getAccountsPage");
        var pageSize = component.get("v.pageSize").toString();
        var pageNumber = component.get("v.pageNumber").toString();
         // set the parameters to method  
        action.setParams({
            'pageSize' : pageSize,
            'pageNumber' : pageNumber
        });
        action.setCallback(this,function(response){
            // store the response return value 
            var state = response.getState();
            if (state === "SUCCESS") {
                var resultData = response.getReturnValue();
                if(resultData.length < component.get("v.pageSize")){
                    component.set("v.isLastPage", true);
                } else{
                    component.set("v.isLastPage", false);
                }
                component.set("v.dataSize", resultData.length);
                component.set("v.data", resultData);
            }
        });
        $A.enqueueAction(action);
    },   
})