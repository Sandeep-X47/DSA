# Brute Force
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

class Solution:

    def printLL(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next

    def deleteNthNodeFromEnd(self, head, N):

        if head is None:
            return None

        # Count nodes
        cnt = 0
        temp = head

        while temp:
            cnt += 1
            temp = temp.next

        # Invalid N
        if N > cnt:
            return head

        # Delete head
        if N == cnt:
            return head.next

        # Find node before target
        pos = cnt - N
        temp = head

        for _ in range(pos - 1):
            temp = temp.next

        # Delete node
        temp.next = temp.next.next

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    sol = Solution()
    head = sol.deleteNthNodeFromEnd(head, N)
    sol.printLL(head)


# Optimal
# Class representing a node in the linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Class to hold the solution logic
class Solution:
    # Function to print the linked list
    def printLL(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next

    # Function to delete the Nth node from the end 
    # using the optimized two-pointer method
    def deleteNthNodeFromEnd(self, head, N):
        # Create a dummy node before head to handle edge cases
        dummy = Node(0, head)

        # Initialize slow and fast pointers at dummy
        slow = dummy
        fast = dummy

        # Move fast pointer N+1 steps ahead to create a gap
        for _ in range(N + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Slow is now at node before target → delete target node
        slow.next = slow.next.next

        # Return updated head
        return dummy.next

# Main driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # Create Solution object
    sol = Solution()

    # Delete the Nth node from the end
    head = sol.deleteNthNodeFromEnd(head, N)

    # Print the modified linked list
    sol.printLL(head)
 