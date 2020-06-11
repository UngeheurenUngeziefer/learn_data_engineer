function randomRange(min, max) {

    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var myRandom = randomRange(5, 15);

console.log(myRandom);
