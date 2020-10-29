({	
    // Функция получения всех аккаунтов
	myAction : function(component, event, helper) {
		var action = component.get("c.getAllAccounts");
        action.setCallback(this, function(a){
            component.set("v.accounts", a.getReturnValue());
        });
        $A.enqueueAction(action);
	},
    
    // Функция получающая список контактов с сервера
    getContactsList : function(component, event, helper) {
        // Помощник доставляет контакты
        helper.fetchContacts(component, event, helper);
    },

    // Функция создания нового контакта
    newContact: function(component, event, helper) {
        // Создание записи
        var createContact = $A.get("e.force:createRecord");
        // Установка параметров
        createContact.setParams({
            "entityApiName": "Contact",
            "defaultFieldValues": {
                "AccountId": component.get("v.recordId")
            }
        });
        // Событие запущено и открыт новый контакт
        createContact.fire();
    },
    
    // Таблица
    init: function(cmp, event, helper) {
        helper.setColumns(cmp);
        helper.setData(cmp);
    },

    // Сортировка
    handleSort: function(cmp, event, helper) {
        helper.handleSort(cmp, event);
    }
})