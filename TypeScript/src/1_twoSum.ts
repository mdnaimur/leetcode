function twoSum(nums: number[], target: number): number[] {
    const map = new Map<number, number>(); // Initialize a Map

    for (let i = 0; i < nums.length; i++) {
        const complement: number = target - nums[i];

        if (map.has(complement)) {
            return [map.get(complement)!, i]; // Return indices
        }

        map.set(nums[i], i); // Store the index of the current number
    }

    return []; // Return empty array if no solution found
}

console.log(twoSum([2, 7, 11, 15], 9)); // Output: [0, 1]
console.log(twoSum([3, 2, 4], 6));      // Output: [1, 2]
console.log(twoSum([3, 3], 6));         // Output: [0, 1]
