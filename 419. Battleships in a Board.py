class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def findShip(board, x, y):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            if board[x][y] == "X":
                board[x][y] = "-"

                for dirs in directions:
                    x_new = x + dirs[0]
                    y_new = y + dirs[1]

                    if x_new >= 0 and x_new < len(board) and y_new >= 0 and y_new < len(board[0]):
                        findShip(board, x_new, y_new)
        
        ship_count = 0

        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[i][k] == "X":
                    ship_count += 1
                    findShip(board, i, k)
        
        return ship_count
