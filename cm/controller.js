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
        
    searchTable : function(cmp,event,helper) {
        var allRecords = cmp.get("v.conList");
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
                
        cmp.set("v.conList",tempArray);
        
        },
            
            
            getAccounts : function(component, event) {
          var action = component.get("c.getContactData");
          action.setCallback(this, function(response) {
              var state = response.getState();
              if (state === "SUCCESS") {
                  component.set("v.conList", response.getReturnValue());
              }
          });
          $A.enqueueAction(action);
      },
  
      sortByName : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.Name.toLowerCase();
                  var nameB = b.Name.toLowerCase();
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.Name.toLowerCase();
                  var nameB = b.Name.toLowerCase();
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
          sortByEmail : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.Email;
                  var nameB = b.Email;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.Email;
                  var nameB = b.Email;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
           sortByCL : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.Contact_Level__c;
                  var nameB = b.Contact_Level__c;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.Contact_Level__c;
                  var nameB = b.Contact_Level__c;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
          sortByAccount : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.AccountId;
                  var nameB = b.AccountId;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.AccountId;
                  var nameB = b.AccountId;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
          sortByOwner : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.OwnerId;
                  var nameB = b.OwnerId;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.OwnerId;
                  var nameB = b.OwnerId;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
          
          
          sortByCB : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.CreatedById;
                  var nameB = b.CreatedById;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.CreatedById;
                  var nameB = b.CreatedById;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      },
          
          sortByCD : function (component, event) {
          var listAccs = component.get("v.conList");
          var sortDirection = component.get("v.sortDirection");
          if (sortDirection == true) {
              listAccs.sort(function (a, b) {
                  var nameA = a.Birthdate;
                  var nameB = b.Birthdate;
                  if (nameA < nameB) {
                      return -1;
                  }
                  if (nameA > nameB) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", false);
              component.set("v.arrow", "utility:arrowdown");
          }else {
              listAccs.sort(function (a, b) {
                  var nameA = a.Birthdate;
                  var nameB = b.Birthdate;
                  if (nameB < nameA) {
                      return -1;
                  }
                  if (nameB > nameA) {
                      return 1;
                  }
                  return 0;
  
              });
              component.set("v.sortDirection", true);
              component.set("v.arrow", "utility:arrowup");
          }
          component.set("v.conList", listAccs);
      }
          
   
   })