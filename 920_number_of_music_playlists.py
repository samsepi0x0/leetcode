class Solution:
    def solve(self, n, goal, k, dp) -> int:
        mod = int(10 ** 9) + 7
        if n == 0 and goal == 0:
            return 1
        if n == 0 or goal == 0:
            return 0
        if dp[n][goal] != -1:
            return dp[n][goal]
        
        p = self.solve(n-1, goal-1, k, dp) * n
        np = self.solve(n, goal-1, k, dp) * max(n-k, 0)

        dp[n][goal] = (p + np) % mod

        return dp[n][goal]
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[-1 for i in range(0, goal+1)] for j in range(0, n+1)]
        return self.solve(n, goal, k, dp)
    
