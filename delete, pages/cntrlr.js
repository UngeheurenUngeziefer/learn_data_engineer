({
  doinit: function(component, helper) {
      var action = component.get('c.getContactData');
      var self = this;
      action.setCallback(this, function(actionResult) {
      component.set('v.conList', actionResult.getReturnValue());
      helper.getAccountsPage(component, helper);
      });
     
    $A.enqueueAction(action);
  },
 
   delete : function(component, event) {
         var action = component.get("c.deleteContact");
         action.setParams({ContactId:event.target.id});
         action.setCallback(this, function(response) {
          component.set("v.conList",response.getReturnValue());
         });
         $A.enqueueAction(action);
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
        
 
 })