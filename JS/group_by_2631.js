// group_by_2631.js

Array.prototype.groupBy = function (fn) {

    const returnObject = {};

    for (const item of this) {
        const key = fn(item);
        if (key in returnObject) {
            returnObject[key].push(item);
        }

        else {
            returnObject[key] = [item]
        }
    }

    return returnObject;

};

// Example usage
const data = [6.1, 4.2, 6.3];

const groupedByFloor = data.groupBy(Math.floor);
console.log(groupedByFloor);
// Output: { '4': [4.2], '6': [6.1, 6.3] }

const names = ['apple', 'banana', 'cherry', 'apricot'];

const groupedByFirstLetter = names.groupBy(item => item[0]);
console.log(groupedByFirstLetter);
// Output: { 'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry'] }