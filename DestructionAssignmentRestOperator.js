const source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
function removeFirstTwo(list) {
  const [ , , ...arr] = list;  // remove 2 first elem
  return arr;
}

const arr = removeFirstTwo(source);
console.log(arr);
console.log(source);