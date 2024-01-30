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
    TreeNode* invertTree(TreeNode* root) {
        stack<TreeNode*> st;
        st.push(root);

        while(!st.empty()) {
            TreeNode* tmp = st.top();
            if (tmp != NULL) {
                
                TreeNode* t = tmp->left;
                tmp->left = tmp->right;
                tmp->right = t;

                st.pop();
                st.push(tmp->left);
                st.push(tmp->right);
            } else {
                st.pop();
            }
        }
        return root;
    }
};
