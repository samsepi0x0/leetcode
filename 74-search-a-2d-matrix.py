class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lb = 0
        ub = 0

        for i in range(0, len(matrix)):
            if (target >= matrix[i][0] and target <= matrix[i][len(matrix[i])-1]):
                lb = 0
                ub = len(matrix[i])-1

                while lb <= ub:
                    mid = lb + (ub - lb) // 2;
                    print(lb, mid, ub, matrix[i][lb], matrix[i][mid], matrix[i][ub])
                    if (matrix[i][mid] == target):
                        return True
                    elif target > matrix[i][mid]:
                        lb = mid + 1
                    else:
                        ub = mid - 1
            else:
                continue
        return False
