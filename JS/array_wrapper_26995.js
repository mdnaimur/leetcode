// array_wrapper_26995.js



/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function (nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function () {
    return this.nums.reduce((acc, num) => acc + num, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function () {
    return `[` + this.nums.join(",") + `]`;

}

//example 

const obj1 = new ArrayWrapper([1, 2, 3]);
const obj2 = new ArrayWrapper([4, 5]);

// Sum the two instances
console.log(obj1 + obj2); // Output: 15

// Convert to string
console.log(String(obj1)); // Output: [1,2,3]
console.log(String(obj2)); // Output: [4,5]
