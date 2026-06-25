# Brute Force
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # Function to detect start of loop using Hash Map
    def detectCycle(self, head):
        # Create a set to store visited nodes
        visited = set()

        # Traverse the list
        while head:
            # If current node already visited, it's the start of cycle
            if head in visited:
                return head

            # Add current node to visited set
            visited.add(head)

            # Move to next node
            head = head.next

        # No cycle found
        return None

# Driver code
if __name__ == "__main__":
    # Creating nodes
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    # Creating a cycle (tail connects to node index 1)
    head.next.next.next.next = head.next

    obj = Solution()
    startNode = obj.detectCycle(head)

    if startNode:
        print("Cycle starts at node with value:", startNode.val)
    else:
        print("No cycle found.")

# Optimal
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # Function to detect the starting node of the loop using Floyd’s algorithm
    def detectCycle(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Traverse while fast and fast.next are not None
        while fast and fast.next:
            # Move slow one step
            slow = slow.next

            # Move fast two steps
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                # Reset slow to head
                slow = head

                # Move both pointers one step to find entry point
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                # Return starting node of cycle
                return slow

        # No cycle found
        return None

# Driver code
if __name__ == "__main__":
    # Create linked list nodes
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    # Create cycle (last node points to node with value 2)
    head.next.next.next.next = head.next

    obj = Solution()
    result = obj.detectCycle(head)

    if result:
        print("Cycle starts at node with value:", result.val)
    else:
        print("No cycle found.")
