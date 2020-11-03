({
    // Инициализирующая функция
    doinit: function(component, helper) {
        var action = component.get('c.getContactData');
        var self = this;
        action.setCallback(this, function(actionResult) {
        component.set('v.conList', actionResult.getReturnValue());
        helper.getAccountsPage(component, helper);
        component.set("v.myRecordID",cmp.get("v.recordId"));
        });
        $A.enqueueAction(action);
    },
   
    // Удаление контакта
    delete: function(component, event) {
        var action = component.get("c.deleteContact");
        action.setParams({ContactId:event.target.id});
        action.setCallback(this, function(response) {
        component.set("v.conList",response.getReturnValue());
        });
        $A.enqueueAction(action);
    },
        
    // Следующая страница
    handleNext : function(component, event, helper) { 
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber+1);
        helper.getAccountsPage(component, helper);
    },
        
    // Предыдущая страница
    handlePrev : function(component, event, helper) {        
        var pageNumber = component.get("v.pageNumber");
        component.set("v.pageNumber", pageNumber-1);
        helper.getAccountsPage(component, helper);
    },

    // Поиск
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
            
    // Получение контактов
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
  
    // Сортировка по имени
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
        
    // Сортировка по email
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
    
    // Сортировка по уровню контакта
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
    
    // Сортировка по аккаунту
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
    
    // Сортировка по владельцу
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
          
          
    // Сортировка по создателю      
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
    
    // Сортировка по дате создания
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
    },
    
    // Создание записи
    createRecord : function (component, event, helper) {
        var createRecordEvent = $A.get("e.force:createRecord");
        createRecordEvent.setParams({
            "entityApiName": "Contact"
        });
        createRecordEvent.fire();
    },
    
    // Применить данные
    submitDetails: function (cmp, event, helper) {
        var nameFieldValue = cmp.find("nameField").set("v.value");
        var emailFieldValue = cmp.find("emailField").set("v.value");
        var contactLevelFieldValue = cmp.find("contactLevelField").set("v.value");
        var accountIdFieldValue = cmp.find("accountIdField").set("v.value");
      	cmp.set("v.isModalOpen", false);	
    },
        
    // Открытие модели
    openModel: function(component, event, helper) {
        component.set("v.isModalOpen", true);
    },
    
    // Закрытие модели
    closeModel: function(component, event, helper) {
        component.set("v.isModalOpen", false);
   },
})