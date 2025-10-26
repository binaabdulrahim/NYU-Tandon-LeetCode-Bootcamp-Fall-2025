'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.'''

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_rows = []
    zero_cols = []
    
    # Step 1: Find all zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)
    
    # Step 2: Zero out rows
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0
    
    # Step 3: Zero out columns
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0