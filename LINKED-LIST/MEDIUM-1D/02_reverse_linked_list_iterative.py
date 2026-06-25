# Brute Force
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to reverse a linked list using stack
    def reverseList(self, head):
        # Stack to store values of nodes
        stack = []

        # Temporary pointer to traverse the list
        temp = head

        # Traverse and push all node values to stack
        while temp:
            stack.append(temp.val)
            temp = temp.next

        # Reset temp back to head
        temp = head

        # Reassign values from stack in reverse order
        while temp:
            temp.val = stack.pop()
            temp = temp.next

        # Return the modified head
        return head

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

# Creating linked list 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

sol = Solution()
head = sol.reverseList(head)
printList(head)


# Optimal Approach
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    # Function to reverse a linked list iteratively
    def reverseList(self, head):
        # Initialize previous pointer to None
        prev = None

        # Start from the head of the list
        temp = head

        # Traverse the list
        while temp:
            # Save the next node
            front = temp.next

            # Reverse the current node's pointer
            temp.next = prev

            # Move prev to current node
            prev = temp

            # Move to the next node
            temp = front

        # Return new head (last node becomes first)
        return prev

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
# Reversing the list
newHead = sol.reverseList(head)

# Printing the reversed list
printList(newHead)
