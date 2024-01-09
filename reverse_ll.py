from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, curr = None, head
        while curr:
            # print(f"curr is: {curr.val}")
            nxt = curr.next ## keep track temporarily
            # if nxt:
            #     print(f"next is: {nxt.val}")
            curr.next = res
            res = curr
            # print(f"reverse head is: {res.val}")
            curr = nxt ## notice i did not do curr.next because on line 14, curr.next is set to None. Instead,
                        ## curr.next is set to temp next, which we got from line 11
            # print("new: ", curr)
            # print()
        return res