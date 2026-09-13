class Solution: # brute force
    def markinfinity(self,matrix,row,column):
            r = len(matrix)
            c = len(matrix[0])
            for i in range(0,r):
                if matrix[i][column] != 0:
                    matrix[i][column] = float("inf")

            for j in range(0,c):
                if matrix[row][j] != 0:
                    matrix[row][j] = float("inf")

    def setZeroes(self, matrix: List[List[int]]) -> None:        
        rows = len(matrix)
        column = len(matrix[0])
        for i in range(0,rows):
            for j in range(0,column):
                if matrix[i][j] == 0:
                    self.markinfinity(matrix,i,j)

        for i in range(0,rows):
            for j in range(0,column):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0


class Solution: #optimal
    def setZeroes(self, matrix: List[List[int]]) -> None:        
        row = len(matrix)
        col = len(matrix[0])
        r = [0]*row
        c = [0]*col
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == 0:
                    r[i] = -1
                    c[j] = -1

        for i in range(0,row):
            for j in range(0,col):
                if r[i] == -1 or c[j] == -1:
                    matrix[i][j] = 0
                    