/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxA = nums[0];
    let sum = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > sum + nums[i]) {
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        maxA = Math.max(maxA, sum);
    }
    
    return maxA;
};
