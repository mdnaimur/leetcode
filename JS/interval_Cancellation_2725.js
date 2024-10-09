// interval_Cancellation_2725.js

var cancellable = function (fn, args, t) {
    let timeObserve;
    var calcelTimesMs;

    fn(...args);

    timeObserve = setInterval(() => {
        fn(...args)
    }, t)

    calcelTimesMs = () => clearInterval(timeObserve);

    return calcelTimesMs

};


// Example usage
const fn = (a, b) => console.log(a + b);
const args = [2, 3];
const t = 2000;  // Delay in milliseconds

const cancelFn = cancellable(fn, args, t);