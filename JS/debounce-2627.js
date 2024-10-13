// debounce-2627.js

var debounce = function (fn, t) {
    let timeLimit;

    return function (...args) {
        if (timeLimit) clearTimeout(timeLimit);

        timeLimit = setTimeout(() => {
            fn(...args);
        }, t)

    }
}




const debouncedFunction = debounce((msg) => console.log(msg), 50);

// Example calls
debouncedFunction('Call at 30ms'); // Call at 30ms
setTimeout(() => debouncedFunction('Call at 60ms'), 30); // Call at 60ms
setTimeout(() => debouncedFunction('Call at 100ms'), 70); // Call at 100ms
