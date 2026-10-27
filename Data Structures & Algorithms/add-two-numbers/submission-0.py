# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currOne, currTwo = l1, l2
        first_number = ""
        while currOne:
            first_number += str(currOne.val)
            currOne = currOne.next

        second_number = ""
        while currTwo:
            second_number += str(currTwo.val)
            currTwo = currTwo.next
        
        num1, num2 = int(first_number[::-1]), int(second_number[::-1])

        new_num = str(num1 + num2)
        new_list = new_num[::-1]

        dummy = ListNode(0)
        curr = dummy

        for i in range(len(new_list)):
            curr.next = ListNode(new_list[i])
            curr = curr.next

        return dummy.next