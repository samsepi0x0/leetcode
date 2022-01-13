class Solution {
    public int maxArea(int[] height) {
        int area = 0;
        
        int x = 0;
        int y = height.length - 1;
        
        while(x < y){
            area = Math.max(area, (y-x)*Math.min(height[x], height[y]));
            if (height[x] < height[y])
                x += 1;
            else
                y -= 1;
        }
        
        return area;
    }
}
