function testLogicalAnd(val) {
    if (val <= 50 && val >= 25) {
        return 'Yes';
    }
    return 'No';
}

function testLogicalOr(val) {
    if (val < 10 || val > 20) {
        return 'Outside';
    }
    return 'Inside';
}

console.log(testLogicalAnd(30));
console.log(testLogicalOr(30));