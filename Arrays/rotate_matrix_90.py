class Solution: #brute force by using more space
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                result[j][n-1-i] = matrix[i][j]
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j] = result[i][j]

#optimal
class Solution: #uses transpose
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0,n):
            matrix[i].reverse()