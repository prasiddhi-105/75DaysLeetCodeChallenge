class Solution(object):
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        boxes = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # Unique identifiers
                row_key = (r, val)
                col_key = (c, val)
                box_key = (r//3, c//3, val)
                
                if row_key in rows or col_key in cols or box_key in boxes:
                    return False
                
                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)
        
        return True