function switchOfStuff(val) {
   var answer = '';
   switch(val) {
      case 'a':
         answer = 'apple';
         break;
      case 'b':
         answer = 'bird';
         break;
      case 'c':
         answer = 'cat';
         break;
      default:
         answer = 'stuff';
         break;
   }
   return answer;
}

console.log(switchOfStuff(2));
