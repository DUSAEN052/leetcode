/**
 * @param {string} moves
 * @return {boolean}
 */
let judgeCircle = function(moves) {
    let arr = [0, 0, 0, 0]
    
    for (let i = 0; i < moves.length; i++) {
        switch (moves.charAt(i)) {
            case 'U':
                arr[0] += 1;
                break;
            case 'D':
                arr[1] += 1;
                break;
            case 'L': 
                arr[2] += 1;
                break;
            case 'R':
                arr[3] += 1;
                break;
        }
    }

    if (arr[0] == arr[1] && arr[2] == arr[3]) {
        return true;
    } else {
        return false;
    }
};
