/**
 * @param {number[]} nums
 * @return {number[]}
 */
let findDuplicates = function(nums) {
    let output = []
    
    if (nums == null) {
        return nums
    }
    
    for (let i = 0; i < nums.length; i++) {
        let index = Math.abs(nums[i]) - 1
        
        if (nums[index] > 0) {
            nums[index] = -nums[index]
        } else {
            output.push(Math.abs(index + 1))
        }
    }
    return output
};
