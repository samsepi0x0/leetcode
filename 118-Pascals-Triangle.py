class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[0 for j in range(i+1)] for i in range(numRows)]
        arr[0][0] = 1
        if numRows == 1:
            return arr
        for i in range(1, numRows):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    arr[i][j] = 1
                    continue
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr
