({
    getColumn : function(component) {        
        component.set('v.columns', [
            {label: 'Name', fieldName: 'Name', type: 'text', sortable: true},
            {label: 'Email', fieldName: 'Email', type: 'Email', sortable: true},
            {label: 'Phone', fieldName: 'Phone', type: 'phone', sortable: true},
            {label: 'Delete Contact', type:  'button', typeAttributes: { iconName: 'utility:delete',  label: 'Del', name: 'deleteRecord', 
                                               title: 'deleteTitle', disabled: false, value: 'test'}}
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
    
    

     sortData: function (cmp, fieldName, sortDirection) {
        var data = cmp.get("v.data");
        var reverse = sortDirection !== 'asc';
        data.sort(this.sortBy(fieldName, reverse));
        cmp.set("v.data", data);
    },
    
    sortBy: function (field, reverse, primer) {
        var key = primer ?
            function(x) {return primer(x[field])} :
            function(x) {return x[field]};
        reverse = !reverse ? 1 : -1;
        return function (a, b) {
            return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
        }
    },
    
    
    
    
})