# Brute Force Approach
class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

# Function to convert a list to a doubly linked list
def convertArr2DLL(arr):
    # Create head node
    head = Node(arr[0])
    
    # Pointer to track previous node
    prev = head

    # Traverse remaining elements
    for i in range(1, len(arr)):
        # Create new node with back reference to prev
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    # Return head of DLL
    return head

# Function to print the doubly linked list
def printDLL(head):
    # Traverse and print each node's data
    while head:
        print(head.data, end=" ")
        head = head.next

# Function to reverse the DLL using stack
def reverseDLL(head):
    # If list is empty or has one node, return as is
    if not head or not head.next:
        return head

    # Stack to hold node data
    stack = []

    # Pointer to traverse list
    temp = head

    # Push all node values to stack
    while temp:
        stack.append(temp.data)
        temp = temp.next

    # Reset temp to head
    temp = head

    # Replace node data with values from stack
    while temp:
        temp.data = stack.pop()
        temp = temp.next

    # Return reversed head
    return head

# Driver code
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print("Doubly Linked List Initially:")
printDLL(head)
head = reverseDLL(head)
print("\nDoubly Linked List After Reversing:")
printDLL(head)


# Optimal
# Class to represent a Node of a doubly linked list
class Node:
    def __init__(self, data):
        # Initialize the data
        self.data = data
        # Pointer to the next node
        self.next = None
        # Pointer to the previous node
        self.prev = None

# Function to convert a list into a doubly linked list
def convert_list_to_dll(arr):
    # Create the head node from the first element
    head = Node(arr[0])
    # Maintain a previous pointer to link backwards
    prev = head

    # Loop through the rest of the elements
    for i in range(1, len(arr)):
        # Create a new node with previous pointer set to 'prev'
        new_node = Node(arr[i])
        new_node.prev = prev
        # Link previous node's next to this node
        prev.next = new_node
        # Move prev forward
        prev = new_node

    # Return the head of the list
    return head

# Function to reverse the doubly linked list
def reverse_dll(head):
    # Initialize a temporary pointer to traverse the list
    temp = None
    # Start from the head
    current = head

    # Traverse till the end of the list
    while current is not None:
        # Swap the next and prev pointers
        temp = current.prev
        current.prev = current.next
        current.next = temp
        # Move to the next node in original list, which is prev now
        current = current.prev

    # After loop, temp will be pointing to the last node’s prev
    # So, adjust head to the new head of the reversed list
    if temp is not None:
        head = temp.prev

    # Return new head
    return head

# Function to print the doubly linked list
def print_dll(head):
    # Traverse and print each node's data
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    head = convert_list_to_dll(arr)
    print("Original DLL:")
    print_dll(head)
    head = reverse_dll(head)
    print("Reversed DLL:")
    print_dll(head)
