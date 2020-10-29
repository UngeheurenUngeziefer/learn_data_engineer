({
    // Функиця доставляющая данные с сервера
        fetchContacts : function(component, event, helper) {
        // Задаём метод переменной
        var action = component.get("c.getContactList");
        // Берём id аккаунта
        var accountId = component.get("v.recordId");
        // Задаём параметры
        action.setParams({
            accountIds: accountId
        });
             
        // Функция ответа
        action.setCallback(this, function(response) {
            // Получаем ответ
            var state = response.getState();
            // Успешный сценарий
            if(state === 'SUCCESS') {
                // Получаем список контактов из ответа и сохраняем в переменную
                var contactList = response.getReturnValue();
                // Назначаем атрибут списка в компонент с значением возвращённым функцией
                component.set("v.contactList", contactList);
            }
            else {
                // Ошибка
                alert('Error in getting data');
            }
        });
        // Добавляем переменную действия в очередь
        $A.enqueueAction(action);
        },
    
    
    
    COLUMNS: [
        { label: 'Name', fieldName: 'name', sortable: true, },
        { label: 'Age', fieldName: 'age', type: 'number', sortable: true, cellAttributes: { alignment: 'left' }, },
        { label: 'Email', fieldName: 'email', type: 'email', sortable: true },
    ],

    DATA: [
        { id: 1, name: 'Billy Simonns', age: 40, email: 'billy@salesforce.com' },
        { id: 2, name: 'Kelsey Denesik', age: 35, email: 'kelsey@salesforce.com' },
        { id: 3, name: 'Kyle Ruecker', age: 50, email: 'kyle@salesforce.com' },
        {
            id: 4,
            name: 'Krystina Kerluke',
            age: 37,
            email: 'krystina@salesforce.com',
        },
    ],
    
    // Назначение столбцов
    setColumns: function(cmp) {
        cmp.set('v.columns', this.COLUMNS);
    },

    // Назначение информации в столбцы
    setData: function(cmp) {
        cmp.set('v.data', this.DATA);
    },

    // Используется для сортировки по Возрасту
    sortBy: function(field, reverse, primer) {
        var key = primer
            ? function(x) {
                  return primer(x[field]);
              }
            : function(x) {
                  return x[field];
              };

        return function(a, b) {
            a = key(a);
            b = key(b);
            return reverse * ((a > b) - (b > a));
        };
    },

    // Сортировка
    handleSort: function(cmp, event) {
        var sortedBy = event.getParam('fieldName');
        var sortDirection = event.getParam('sortDirection');

        var cloneData = this.DATA.slice(0);
        cloneData.sort((this.sortBy(sortedBy, sortDirection === 'asc' ? 1 : -1)));
        
        cmp.set('v.data', cloneData);
        cmp.set('v.sortDirection', sortDirection);
        cmp.set('v.sortedBy', sortedBy);
    }
})