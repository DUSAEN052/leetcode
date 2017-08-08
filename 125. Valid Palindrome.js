/**
 * @param {string} s
 * @return {boolean}
 */
let isPalindrome = function(s) {
    if (s === "" || s === " ") {
        return true
    }
    
    let st = s.replace(/\W+/g, '').toLowerCase()
    let sr = st.split("").reverse("").join("")
    
    return (st == sr)
};
