class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for i in range(ROWS):
            for j in range(COLS):

                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # set the first row's element to zero
                    if i > 0:
                        matrix[i][0] = 0 # set the first column's elements to zero except for [0][0]
                    else:
                        rowZero = True # for [0][0]

        # zero out the elements except the first row and column
        for i in range(1, ROWS):
            for j in range(1, COLS):
                
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # if the 0th element is 0; zero out whole column
        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        #  if the rowZero is True; zero out whole row
        if rowZero:
            for j in range(COLS):
                matrix[0][j] = 0