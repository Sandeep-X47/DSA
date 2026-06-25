# Brute Force
# Node class represents a node in a linked list
class Node:
    # Constructor with data and optional next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

# Solution class containing the delete function
class Solution:
    # Function to delete the middle node of a linked list
    def deleteMiddle(self, head):
        # Initialize a temporary node to traverse the linked list
        temp = head
        # Variable to hold the number of nodes in the linked list
        n = 0
        # Loop to count the number of nodes in the linked list
        while temp is not None:
            n += 1
            temp = temp.next
        # Calculate the index of the middle node
        res = n // 2
        # Reset the temporary node to the beginning of the linked list
        temp = head
        # Loop to find the middle node to delete
        while temp is not None:
            res -= 1
            # If the middle node is found
            if res == 0:
                # Create a pointer to the middle node
                middle = temp.next
                # Adjust pointers to skip the middle node
                temp.next = temp.next.next
                # Exit the loop after deleting the middle node
                break
            # Move to the next node in the linked list
            temp = temp.next
        # Return the head of the modified linked list
        return head

# Function to print the linked list
def printLL(head):
    # Initialize a temporary pointer
    temp = head
    # Traverse the linked list and print data
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    # Print a newline after the list
    print()

# Driver code
if __name__ == "__main__":
    # Creating a sample linked list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Display the original linked list
    print("Original Linked List:", end=" ")
    printLL(head)

    # Create a Solution object
    obj = Solution()
    # Deleting the middle node
    head = obj.deleteMiddle(head)

    # Displaying the updated linked list
    print("Updated Linked List:", end=" ")
    printLL(head)


# Optimal
# Node class represents a node in the linked list
class Node:
    # Constructor with data and next pointer
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Solution class contains method to delete middle node
class Solution:
    # Function to delete the middle node
    def deleteMiddle(self, head):
        # If list has only one node, delete it
        if head is None or head.next is None:
            return None

        # Initialize slow pointer to head
        slow = head

        # Initialize fast pointer two steps ahead
        fast = head.next.next

        # Traverse until fast reaches end
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Bypass the middle node
        slow.next = slow.next.next

        # Return head of updated list
        return head

# Function to print linked list
def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver function
if __name__ == "__main__":
    # Creating linked list 1->2->3->4->5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Printing original list
    print("Original Linked List:", end=" ")
    printLL(head)

    # Deleting middle node
    obj = Solution()
    head = obj.deleteMiddle(head)

    # Printing updated list
    print("Updated Linked List:", end=" ")
    printLL(head)
