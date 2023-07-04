class Solution {
    public int maxArea(int[] height) {
        // O(n^2) --> TLE
        // int max_area = 0;
        // for(int i = 0; i < height.length - 1; i++){
        //     for(int j = i+1; j < height.length; j++){
        //         int l = j - i;
        //         int b = Math.min(height[i], height[j]);
        //         int tarea = l*b;
        //         max_area = Math.max(tarea, max_area);
        //     }
        // }
        // return max_area;

        // O(log N)
        int l = 0;
        int r = height.length - 1;
        int area = 0;

        while (l < r){ 
            int len = height[l] < height[r] ? height[l] : height[r];
            int bred = r - l;
            area = Math.max(area, len*bred);
            //System.out.println(l + "\t" + r + "\t" + height[l] + "\t" + height[r] + "\t" +(len*bred) + "\t" + area);
            if(height[l] <= height[r])
                l += 1;
            else if(height[l] > height[r])
                r -= 1;
        }
        return area;

    }
}
