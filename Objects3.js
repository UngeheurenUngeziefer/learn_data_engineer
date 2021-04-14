function phoneticLookup(val) {
    var result = '';

    var lookup = {
        'alpha': 'Adams',
        'bravo': 'Boston'
    };
    result = lookup[val];

    return result;
}

console.log(phoneticLookup('alpha'))