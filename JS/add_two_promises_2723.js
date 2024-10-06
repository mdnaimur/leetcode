// add_two_promises_2723.js

// method 1
// function sumTwoPromises(promise1, promise2) {
//     return Promise.all([promise1, promise2]).then(value => value[0] + value[1]);
// }

// method 2

// var addTwoPromises = async function (promise1, promise2) {
//     try {
//         const [res1, res2] = await Promise.all([promise1, promise2]);

//         return res1 + res2;
//     }
//     catch (e) {
//         console.error(e)
//     }
// }


//method 3

var addTwoPromises = async function (promise1, promise2) {
    try {
        return await promise1 + await promise2;
    } catch (error) {
        console.error(error);
        throw error; // Rethrow the error to maintain the behavior of propagating the error to the caller
    }
};



// Example usage
const promise1 = Promise.resolve(3);
const promise2 = Promise.resolve(5);

sumTwoPromises(promise1, promise2).then(result => {
    console.log(result);  // Output: 8
});