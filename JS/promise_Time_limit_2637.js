// promise_Time_limit_2637.js

var timeLimit = function (fn, t) {

    return async function (...args) {
        return new Promise((resolve, reject) => {
            const timeout = setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)

            fn(...args).then(result => {
                clearTimeout(timeout);
                resolve(result)
            }).catch(err => {
                clearTimeout(timeout);
                reject(err);
            })
        })
    }
}

const limitedFunction = timeLimit(async (n) => {
    return new Promise(resolve => setTimeout(() => resolve(n), 1000));
}, 500);

limitedFunction(10)
    .then(result => console.log(result))
    .catch(err => console.error(err));  // Output: "Time Limit Exceeded"
