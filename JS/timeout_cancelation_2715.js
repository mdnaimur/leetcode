// timeout_cancelation_2715.js


var cancellable = function (fn, args, t) {

    let timeoutId;
    timeoutId = setTimeout(() => {
        fn(...args);
    }, t)

    return function cancelFn() {
        if (timeoutId) {
            clearTimeout(timeoutId);
            timeoutId = null;
        }
    }

};

// Example usage
const fn = (a, b) => console.log(a + b);
const args = [2, 3];
const t = 2000;  // Delay in milliseconds

const cancelFn = cancellable(fn, args, t);