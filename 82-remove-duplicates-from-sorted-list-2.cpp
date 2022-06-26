/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL)
            return head;
        ListNode* new_head = new ListNode();
        new_head->next = head;
        ListNode* prev = new_head;
        ListNode* temp = head;
        
        while(temp != NULL){
            while(temp->next != NULL && temp->val == temp->next->val){
                temp = temp->next;
            }
            if(prev->next == temp){
                prev = prev->next;
            }
            else{
                prev->next = temp->next;
            }
            temp = temp->next;
        }
        return new_head->next;
    }
};
