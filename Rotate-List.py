/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::rotateRight(ListNode* A, int B) {
    
    if (NULL == A)
    {
        return A;
    }

    ListNode* end = NULL;
    ListNode* p1 = A;

    int length = 1;
    while (p1)
    {
        if (NULL == p1->next)
        {
            p1->next = A;
            break;
        }
        p1 = p1->next;
        ++length;
    }

    if (B > length)
    {
        B = B % length;
    }
    p1 = A;
    for (int i = 0; i < (length - 1 - B); ++i)
    {
        p1 = p1->next;
    }

    A = p1->next;
    p1->next = NULL;

    return A;
}