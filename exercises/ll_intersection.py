from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        copyA = headA
        copyB = headB
        lenA = 0
        lenB = 0

        ## first we get the length of the two linked lists
        while copyA:
            lenA += 1
            copyA = copyA.next
        while copyB:
            lenB += 1
            copyB = copyB.next

        if lenA > lenB:
            shorter = lenB
            shorterLL = headB
            longer = lenA
            longerLL = headA
        else:
            shorter = lenA
            shorterLL = headA
            longer = lenB
            longerLL = headB

        # print(f"Longer linked list: {longerLL} and size is: {longer}")
        # print(f"shorter linked list: {shorterLL} and size is: {shorter}")
        # print()
        diff = longer - shorter
        count = 0
        ## then we skip the longer linked list by the value of diff
        while count != diff and longerLL:
            count += 1
            longerLL = longerLL.next

        pointerLong = longerLL
        pointerOther = shorterLL
        # print(f"Longer linked list will start from : {pointerLong}")
        # print(f"Shorter linked list is: {pointerOther}")
        # print()
        while pointerLong:
            #print(f"long current: {pointerLong.val} and short current: {pointerOther.val}")
            if id(pointerLong) == id(pointerOther): # check by memory address not the value
                return pointerLong
            pointerLong = pointerLong.next
            pointerOther = pointerOther.next
        return None
