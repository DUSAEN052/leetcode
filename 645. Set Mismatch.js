/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    let a = new Set();
    let b = 0;
    let output = [];
    
    for (let i = 0; i < nums.length; i++) {
        if (a.has(nums[i])) {
            b = nums[i];
            output[0] = b;
        } else {
            a.add(nums[i]);
        }
    }
    
    for (let k = 1; i < nums.length + 1; k++) {
         if (!a.has(k)) {
             output[1] = k;
             return output;
         }
    }
    
    return output;
};
