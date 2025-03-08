function containsDuplicate(nums: number[]): boolean {
    const sortsNums = new Set<number>();

    for (let num of nums) {
      if (sortsNums.has(num)){
            return true;
      }
      sortsNums.add(num);
    }
    return false;

};




/***
 * this code is time limit 
 * O(n^2) run time 
 * 
 *  ***/

// function containsDuplicate(nums: number[]): boolean {

//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] == nums[j]) {
//                 return true;
//             }
//         }
//     }

//     return false;

// };

