class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if ((r*c) != (len(mat)*len(mat[0]))) or (r == len(mat) and c == len(mat[0])):
            return mat
        newMat = [[0 for j in range(c)] for i in range(r)]
        i_old = j_old = 0
        for i in range(r):
            for j in range(c):
                newMat[i][j] = mat[i_old][j_old]
                j_old += 1
                if j_old == len(mat[i_old]):
                    i_old += 1
                    j_old = 0
        return newMat
