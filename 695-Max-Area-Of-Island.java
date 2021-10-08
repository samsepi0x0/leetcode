class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        boolean visited[][] = new boolean[grid.length][grid[0].length];
        int m = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                m = Math.max(m, dfs(grid, i, j, visited));
            }
        }
        return m;
    }
    public int dfs(int[][] grid, int sr, int sc, boolean[][] visited){
        int rows = grid.length;
        int cols = grid[0].length;
        
        if (sr < 0 || sr >= rows || sc < 0 || sc >= cols || grid[sr][sc] != 1 || visited[sr][sc]){
            return 0;
        }
        
        visited[sr][sc] = true;
        
        return 1 + dfs(grid, sr+1, sc, visited) + dfs(grid, sr-1, sc, visited) +  dfs(grid, sr, sc+1, visited) + dfs(grid, sr, sc-1, visited) ;
    }
}
