 function numberSize(num) {
     if (num < 5) {
         result = 'Tiny number';
     } else if (num < 10) {
         result = 'Small number';
     } else if (num < 15) {
        result = 'Medium number';
     } else if (num < 20) {
        result = 'Large number';
     } else {
        result = 'Huge number';
     }
     console.log(result)
}

numberSize(1)
numberSize(5)
numberSize(10)
numberSize(19)
numberSize(22)
