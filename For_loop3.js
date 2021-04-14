function multiplyAll(arr) {
    var product = 1;

    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr[i].length; j++) {
            product *= arr[i][j]
        }
    }
    return product;
}

var result = multiplyAll([[1, 2],[3, 4],[5, 6, 7]]);

console.log(result);
