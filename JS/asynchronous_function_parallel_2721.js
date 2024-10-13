// asynchronous_function_parallel_2721.js


var promiseAll = function (functions) {

    return new Promise((resolve, reject) => {
        const results = [];
        let completePromises = 0;
        // If the array is empty, resolve with an empty array
        if (functions.length === 0) {
            resolve(results);
        }

        functions.forEach((fn, index) => {
            fn()
                .then((value) => {
                    results[index] = value;
                    completePromises++;

                    if (completePromises === functions.length) {
                        resolve(results);
                    }
                }).catch((error) => {
                    // If any promise is rejected, reject the final promise with the error
                    reject(error);
                });
        })
    })

};


/// example code 

const asyncFunctions = [
    () => new Promise((resolve) => setTimeout(() => resolve('A'), 100)),
    () => new Promise((resolve) => setTimeout(() => resolve('B'), 200)),
    () => new Promise((resolve) => setTimeout(() => resolve('C'), 150))
];

promiseAll(asyncFunctions)
    .then((result) => console.log(result)) // Expected output: ['A', 'B', 'C']
    .catch((error) => console.log(error));
