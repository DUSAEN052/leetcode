/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
let merge = function(nums1, m, nums2, n) {
    let n1 = m - 1
    let n2 = n - 1
    let nm = m + n - 1
    
    while (n1 >= 0 && n2 >= 0) {
        if (nums2[n2] > nums1[n1]) {
            nums1[nm] = nums2[n2]
            n2--
            nm--
        } else {
            nums1[nm] = nums1[n1]
            n1--
            nm--
        }
    }
    
    while (n2 >= 0) {
        nums1[nm] = nums2[n2]
        nm--
        n2--
    }
};
