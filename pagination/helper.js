({
    getColumn : function(component) {        
        component.set('v.columns', [
            {label: 'Name', fieldName: 'Name', type: 'text'},
            {label: 'AccountNumber', fieldName: 'AccountNumber', type: 'text'},
            {label: 'Industry', fieldName: 'Industry', type: 'text'},
            {label: 'Phone', fieldName: 'Phone', type: 'phone'}           
        ]);
    },
     
    getAccounts : function(component, helper) {
        var action = component.get("c.getAccounts");
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