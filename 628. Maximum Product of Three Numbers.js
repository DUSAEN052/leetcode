/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let sorted = nums.sort(function(a, b) {
        return a - b;
    });
    let len = sorted.length;
    let output1 = sorted[len - 1] * sorted[len - 2] * sorted[len - 3];
    let output2 = sorted[0] * sorted[1] * sorted[len - 1] ;
    let output = Math.max(output1, output2);
    
    return output;
};
