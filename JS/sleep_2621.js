// sleep_2621.js

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));

}

// Example usage:
sleep(20000).then(() => {
    console.log('Executed after 2 seconds');
});