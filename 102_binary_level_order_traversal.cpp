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
    vector<vector<int>> result;
    void levelTraversal(TreeNode* root, int height) {
        if (root == NULL)
            return;
        if (height >= result.size()) {
            vector<int> r;
            result.push_back(r);
        }
        result[height].push_back(root->val);
        levelTraversal(root->left, height + 1);
        levelTraversal(root->right, height + 1);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {    
        levelTraversal(root, 0);
        return result;
    }
};
