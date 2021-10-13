class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int c1=0,c2=0,e1=-1,e2=-1;
        for(int element : nums)
        {
            if(e1==element)
                c1++;
            else if(e2==element)
                c2++;
            else if(c1==0)
            {
                e1=element;
                c1=1;
            }
            else if(c2==0)
            {
                e2=element;
                c2=1;
            }
            else
            {
                c1--;
                c2--;
            }
        }
        List<Integer> res = new ArrayList<Integer>();
        int count1=0,count2=0;
        for(int element : nums)
        {
            if(e1==element)
                count1++;
           else if(e2==element)
                count2++;
                
        }
        if(count1> nums.length/3)
            res.add(e1);
        if(count2>nums.length/3)
            res.add(e2);
        return res;
        
    }
}