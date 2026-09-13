class Solution: 
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return []
        top = 0
        bot = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while top <= bot and left <= right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top,bot+1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bot:#edge case
                for i in range(right,left -1, -1):
                    result.append(matrix[bot][i])
                bot -= 1
            if left <= right:#edge case
                for i in range(bot,top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result