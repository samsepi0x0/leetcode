class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1]:
                low, high = 0, len(matrix[i]) - 1
                while low <= high:
                    mid = (low + high) // 2
                    
                    if matrix[i][mid] == target:
                        return True
                    
                    if matrix[i][mid] < target:
                        low = mid + 1
                    
                    else:
                        high = mid - 1
                        
        return False
                
