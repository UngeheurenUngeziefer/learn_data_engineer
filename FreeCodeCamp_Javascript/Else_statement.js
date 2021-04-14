function testElse(val) {
    if (val > 5) {
        result = 'Bigger than 5';
    } else if (val == 5) {
        result = 'Equal 5';
    } else {
        result = 'Lesser than 5';
    }
    return result
}

console.log(testElse(1))
console.log(testElse(5))
console.log(testElse(6))