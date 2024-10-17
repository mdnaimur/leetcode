// sory_by_2724.js


var sortBy = function (arr, fn) {

    return arr.sort((a, b) => fn(a) - fn(b))
};

//return arr.sort((a, b) => fn(a) - fn(b))

// Example usage
const data = [5, 4, 1, 2, 3];

console.log(sortBy(data))