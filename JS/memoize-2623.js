// memoize-2623.js


function memoize(fn) {
    const memo = {};

    return function (...args) {
        const value = JSON.stringify(args);

        if (value in memo) {
            console.log("Fetching from cache:", value); // Optional: to see when cache is used

            return memo[value];
        }

        const result = fn(...args) //fn.apply(this,args)
        memo[value] = result

        return result;


    }
}


// Test functions
function sum(a, b) {
    return a + b;
}

function fib(n) {
    if (n <= 1) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Memoized versions of the functions
const memoizedSum = memoize(sum);
const memoizedFib = memoize(fib);
const memoizedFactorial = memoize(factorial);

// Test cases
console.log("Testing sum function:");
console.log(memoizedSum(3, 2)); // Output: 5
console.log(memoizedSum(2, 3)); // Output: 5 (new calculation)
console.log(memoizedSum(3, 2)); // Output: 5 (from cache)

console.log("Testing fib function:");
console.log(memoizedFib(5)); // Output: 8 (fib(5) is 8)
console.log(memoizedFib(6)); // Output: 13 (fib(6) is 13)
console.log(memoizedFib(5)); // Output: 8 (from cache)

console.log("Testing factorial function:");
console.log(memoizedFactorial(5)); // Output: 120
console.log(memoizedFactorial(6)); // Output: 720
console.log(memoizedFactorial(5)); // Output: 120 (from cache)
