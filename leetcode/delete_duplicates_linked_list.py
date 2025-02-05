# Definition for singly-linked list.
# type: ignore
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        (1) -> (1) -> (1) -> (1) -> (2)
        """
        if head is None:
            return None

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next

            print(head.val)

            head = head.next


if __name__ == "__main__":
    print(Solution().deleteDuplicates(ListNode(2, ListNode(3, ListNode(4)))))
