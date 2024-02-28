/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int leftVal, maxD;
    void solve(TreeNode* root, int d) {
        if (root == NULL)
            return;
        solve(root->left, d+1);
        solve(root->right, d+1);
        if (d > maxD){
            maxD = d;
            leftVal = root->val;
        }
    }
    int findBottomLeftValue(TreeNode* root) {
        leftVal = root->val;
        maxD = 0;
        solve(root, 0);
        return leftVal;
    }
};
