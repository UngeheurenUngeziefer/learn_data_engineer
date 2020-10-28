({
	// Method to be called on component initialization
    doInit: function(component, event, helper) {
        helper.fetchOppHelper(null, component);
    },
    
    // Method to perform search on opportunities
    searchOpportunities: function(component, event, helper) {
        var searchValue = component.find('searchField').get('v.value');
        helper.fetchOppHelper(searchValue, component);
    }
    
})