const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;
(function() {
  arr2 = [...arr1]; // spread operator
  arr1[0] = 'potato'
})();
console.log(arr2);
console.log(arr1);