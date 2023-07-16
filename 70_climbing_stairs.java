class Solution {
    public int climbStairs(int n) {
        // // Simplest solution where type to reach n stairs is type to reach n-1 and n-2 stairs. Takes too much time though.
        // if(n <= 2)
        //     return n;
        // return climbStairs(n-1) + climbStairs(n-2);
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        arr.add(2);
        return climbStairs(n, arr);
    }
    public int climbStairs(int n, ArrayList<Integer> map){
        if(n <= map.size())
            return map.get(n-1);
        else{
            int s = climbStairs(n-1, map) + climbStairs(n-2, map);
            map.add(s);
            return s;
        }  
    }
}
