function testStrict(val) {
    if (val === 7) {
        return 'Equal';
    }
    return 'Not Equal';
}

console.log(testStrict('7'));

// 7 == 7       equal str and int
// 7 === '7'    equal int
