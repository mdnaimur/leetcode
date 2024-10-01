//returnLengthArgumentsPassed-2703.js


var argumentsLength = function (...args) {
    n = args.length
    return n;
};

console.log(argumentsLength(1, 2, 3));  // Output: 3