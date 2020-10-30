({
    fetchOppHelper: function(searchVal, component) {
        component.set('v.columnsToDisplay', [
            {label: 'Opportunity Name', fieldName: 'Name', type: 'text'},
            {label: 'Close Date', fieldName: 'CloseDate', type: 'date'},
            {label: 'Amount', fieldName: 'Amount', type: 'currency'},
        ]);

        var action = component.get('c.fetchOpportunity');
        action.setParams({
            'searchKeyWord': searchVal
        });

        action.setCallback(this, function(response){
            var state = response.getState();
            if (state === 'SUCCESS') {
                component.set('v.lstOpportunity', response.getReturnValue());
            } else {
                alert('Error');
            }
        });
        $A.enqueueAction(action);
    }

})