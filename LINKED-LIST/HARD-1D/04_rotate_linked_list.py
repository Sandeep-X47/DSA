# Brute Force
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the list to the right by k positions
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If list is empty or has one node or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Repeat the rotation k times
        for _ in range(k):
            # Initialize two pointers
            curr = head
            prev = None

            # Traverse to the last node
            while curr.next:
                prev = curr
                curr = curr.next

            # Remove last node and move it to front
            prev.next = None
            curr.next = head
            head = curr

        # Return the rotated list
        return head

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

# Create linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
k = 2
newHead = sol.rotateRight(head, k)
printList(newHead)


# Optimal
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the linked list to the right by k places
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If list is empty or has only one node or no rotation
        if not head or not head.next or k == 0:
            return head

        # Calculate the length and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Make it a circular linked list
        tail.next = head

        # Calculate effective rotations
        k = k % length

        # Find the new tail (length - k steps)
        stepsToNewTail = length - k
        newTail = head
        for _ in range(stepsToNewTail - 1):
            newTail = newTail.next

        # Set new head
        newHead = newTail.next

        # Break the circle
        newTail.next = None

        return newHead

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Create linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
obj = Solution()
newHead = obj.rotateRight(head, k)
printList(newHead)
