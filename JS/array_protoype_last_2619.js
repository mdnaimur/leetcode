// array_protoype_last_2619.js


Array.prototype.last = function () {
    if (this.length <= 0) {
        return -1
    }

    return this.length;
}

// Example usage
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.last()); // Output: 5

let emptyArray = [];
console.log(emptyArray.last()); // Output: -1