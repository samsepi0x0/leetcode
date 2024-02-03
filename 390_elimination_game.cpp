class Solution {
public:
    int lastRemaining(int n) {
        if (n == 1)
            return n;
        // head to point to start of list;
        int h = 1;
        // step size, increases times 2 each iteration
        int st = 1;
        // are we moving from the left or the right?
        bool left = true;
        while (n != 1) {
            if (left){ // we are moving from the left
                h += st; // increment the head, as it will move
                left = false;
            } else {
                if (n % 2 != 0) // total number of elements when moving from right are odd, head will move
                    h += st;
                left = true;
            }
            st *= 2; // step size doubles each iteration
            n /= 2; // half the list remains after each iteration
        }
        return h; // return head.
    }
};
