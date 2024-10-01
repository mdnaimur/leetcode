// allowOneFunctionCall-2666.js


var once = function (fn) {
    let called = false

    return function (...args) {

        if (!called) {
            called = true

            return fn(...args)
        }
    }
}

const myFunction = (x) => x * 2;
const onceFunction = once(myFunction);

console.log(onceFunction(3));  // Output: 6
console.log(onceFunction(3)); 