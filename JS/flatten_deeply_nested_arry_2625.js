// flatten_deeply_nested_arry_2625.js

var flat = function (arr, n) {

    let res = []
    const flattening = (nums, depth) => {
        for (const num of nums) {
            if (Array.isArray(num) && depth > 0) {
                flattening(num, depth - 1)
            }
            else {
                res.push(num);
            }
        }
    }
    flattening(arr, n);
    return res;
}


// Example: 
let arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
let depth = 2;
console.log(flat(arr, depth)); 