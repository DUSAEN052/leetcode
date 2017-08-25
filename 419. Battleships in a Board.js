/**
 * @param {character[][]} board
 * @return {number}
 */
let countBattleships = function(board) {
    let output = 0
    
    for (let i = 0; i < board.length; i++) {
        for (let k = 0; k < board[i].length; k++) {
            if (board[i][k] == 'X') {
                flood(board, i, k)
                output++
            }
        }
    }
    return output
    
    function flood(board, i, k) {
        if (i >= 0 && k >= 0  && i < board.length && k < board[i].length && board[i][k] == 'X') {
            board[i][k] = '*'
            flood(board, i, k + 1)
            flood(board, i, k - 1)
            flood(board, i + 1, k)
            flood(board, i - 1, k)
        }
    }
};
