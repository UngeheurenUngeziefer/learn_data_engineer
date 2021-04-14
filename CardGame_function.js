var count = 0;

function cc(card) {
   switch(card) {
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
         count++;
         break;
      case 10:
      case 'J':
      case 'Q':
      case 'K':
      case 'A':
         count--;
         break;
   }

   var holdbet = 'Hold'
   if (count > 0) {
      holdbet = 'Bet'
   }

   return count + ' ' + holdbet;
}


cc(2); cc(3); cc(7); cc('K'); cc('A');
console.log(cc('K'))