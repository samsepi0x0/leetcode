class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target >= i[0] or target <= i[len(i) - 1]:
                for j in i:
                    if target == j:
                        return True
        return False
