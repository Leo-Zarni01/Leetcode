from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        if list1 is not None and list2 is not None:
            first_head = list1.val
            second_head = list2.val
            
            if first_head < second_head:
                starting_list = list1
                other_list = list2
            else:
                starting_list = list2
                other_list = list1
            prev = head
            prev.next = starting_list
            dummy = other_list
            # head.next = starting_list
            while starting_list:
                print("Current main list: ", starting_list)
                while dummy:
                    #print(f"Comparing main list value: {starting_list.val} with secondary value: {dummy.val}")
                    if (dummy.val >= starting_list.val):
                        dummy_temp = dummy.next
                        
                        #print(dummy.val, " is greater than or equal to ", starting_list.val)
                        ## remove and attach to main list
                        
                        temp = starting_list.next
                        #print("The unchained ones...", temp)
                        starting_list.next = dummy
                        #print("After adding...", starting_list)
                        ## dummy still works up till here
                        starting_list.next.next = temp
                        dummy = dummy_temp
                        # print("Dummy After: ", dummy)
                        # print("Starting_list after: ", starting_list)
                        break
                    else:
                        dummy = dummy.next
                ## after inserting, check for inversions, i.e, is newly inserted head greater than its neighbor?
                neighbor = starting_list.next
                if neighbor is not None:
                    while neighbor.val < starting_list.val and (starting_list is not None and starting_list.next is not None):
                        print(f"Current head is {starting_list.val} and its neighbor is: {neighbor.val}")
                        print(f"{starting_list.val} > {neighbor.val}")
                        temp_neighbor = starting_list.next
                        print("neighbor: ", temp_neighbor)
                        starting_list.next = starting_list.next.next
                        print("new neighbor: ", starting_list.next)
                        temp_neighbor.next = starting_list
                        print("At the end: ", temp_neighbor.next)
                        starting_list = temp_neighbor
                        prev = prev.next
                        # if starting_list is not None and starting_list.next is not None:
                        #     temp_neighbor.next.next = starting_list.next
                        print("Starting_list after swapping: ", starting_list)
                print()
                starting_list = starting_list.next
            return head.next
        else:
            if list1 is None:
                return list2
            elif list2 is None:
                return list1