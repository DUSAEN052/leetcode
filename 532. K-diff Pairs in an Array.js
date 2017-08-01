/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    let output = 0;
    let aset = new Set();
    let arr = new Map();
    
    if (k < 0) {
        return 0;
    }
    
    if (k == 0) {
        for (let b = 0; b < nums.length; b++) {
            if (aset.has(nums[b])) {
                arr.set(nums[b], 0);
                aset.delete(nums[b]);
            } else {
                aset.add(nums[b]);
            }
        }
        
        return arr.size;
    }
    
    for (let i = 0; i < nums.length; i++) {
        aset.add(nums[i]);
    }
    
    for (let j of aset) {
        let c = j - k;
        
        if (aset.has(c)) {
            if (!(arr.has(c) && arr.get(c) == j || arr.has(j) && arr.get(j) == c)) {
                arr.set(c, j);
            }
        }
    }
    
    for (let h of aset) {
        let c = h + k;
        
        if (aset.has(c)) {
            if (!(arr.has(c) && arr.get(c) == h|| arr.has(h) && arr.get(h) == c)) {
                arr.set(c, h);
            }
        }
    }
    
    return arr.size;
};
