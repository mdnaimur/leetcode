//two_arry_2722.js

var join = function (arr1, arr2) {
    const combinearray = arr1.concat(arr2); // Combine both arrays
    const merge = {}; // Object to store merged items by id

    combinearray.forEach((obj) => {
        const id = obj.id;

        if (!merge[id]) {
            merge[id] = { ...obj }; // If id doesn't exist, create new object
        } else {
            merge[id] = { ...merge[id], ...obj }; // If id exists, merge the existing object with new one
        }
    });

    const joinarray = Object.values(merge); // Get all values from the merge object
    joinarray.sort((a, b) => a.id - b.id); // Sort by id

    return joinarray;
};

// Example data with id properties
const data1 = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
];

const data2 = [
    { id: 2, age: 30 },
    { id: 3, name: 'Charlie', age: 25 },
];

console.log(join(data1, data2));
