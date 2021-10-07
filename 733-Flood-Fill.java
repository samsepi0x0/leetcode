class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        boolean visited[][] = new boolean[image.length][image[0].length];
        dfs(image, sr, sc, newColor, image[sr][sc], visited);
        return image;
    }
    public void dfs(int[][] image, int sr, int sc, int newColor, int orig_color, boolean[][] visited){
        int rows = image.length;
        int cols = image[0].length;
        
        if(sc < 0 || sc >= cols || sr < 0 || sr >= rows || image[sr][sc] != orig_color || visited[sr][sc])
            return;
        
        visited[sr][sc] = true;
        image[sr][sc] = newColor;
        
        dfs(image, sr+1, sc, newColor, orig_color, visited);
        dfs(image, sr-1, sc, newColor, orig_color, visited);
        dfs(image, sr, sc+1, newColor, orig_color, visited);
        dfs(image, sr, sc-1, newColor, orig_color, visited);
    }
}
