// Object-empty-2727.js

var isEmpty = function (obj) {

    if (Array.isArray(obj)) {
        return obj.length === 0;
    }
    else {
        return Object.keys(obj).length === 0;
    }

    return false;

};

// Examples
console.log(isEmpty([]));          // true (empty array)
console.log(isEmpty([1, 2, 3]));   // false (non-empty array)
console.log(isEmpty({}));          // true (empty object)
console.log(isEmpty({ a: 1 }));    // false (non-empty object)