# Define a Node class for doubly linked list
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

# Function to convert an array to a doubly linked list
def convertArr2DLL(arr):
    head = Node(arr[0])  # Create the head node with the first element
    prev = head  # Initialize 'prev' to the head node

    # Traverse the array to create the doubly linked list
    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)  # Create a new node
        prev.next = temp  # Set 'next' of the previous node to the new node
        prev = temp  # Move 'prev' to the new node

    return head  # Return the head of the doubly linked list

# Function to print the elements of the doubly linked list
def printList(head):
    while head:
        print(head.data, end=" ")  # Print the data of the current node
        head = head.next  # Move to the next node
    print()  # New line after printing the list

# Function to insert a new node at the tail of the doubly linked list
def insertAtTail(head, k):
    newNode = Node(k)  # Create a new node with data 'k'

    if not head:
        return newNode  # If the list is empty, return the new node as the head

    tail = head
    while tail.next:
        tail = tail.next  # Traverse to the last node of the list

    tail.next = newNode  # Connect the new node to the last node
    newNode.back = tail  # Set the 'back' pointer of the new node to the previous node
    return head  # Return the head of the modified list

# Driver code
if __name__ == "__main__":
    arr = [12, 5, 8, 7, 4]  # Initialize an array
    head = convertArr2DLL(arr)  # Convert the array to a doubly linked list

    print("Doubly Linked List Initially:")
    printList(head)  # Print the doubly linked list

    print("\nDoubly Linked List After Inserting at the tail with value 10:")
    head = insertAtTail(head, 10)  # Insert a node with value 10 at the end
    printList(head)  # Print the updated doubly linked list