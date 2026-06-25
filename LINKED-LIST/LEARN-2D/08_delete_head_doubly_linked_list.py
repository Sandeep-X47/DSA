# Node structure for DLL
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class Solution:
    # Function to delete tail of DLL
    def deleteTail(self, head):
        # If list is empty
        if not head:
            return None

        # If only one node present
        if not head.next:
            return None

        # Traverse to the last node
        temp = head
        while temp.next:
            temp = temp.next

        # Update second last node's next to None
        temp.prev.next = None

        # Return head
        return head

# Driver code
if __name__ == "__main__":
    # Create a sample DLL: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    obj = Solution()
    head = obj.deleteTail(head)

    # Print list after deletion
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
