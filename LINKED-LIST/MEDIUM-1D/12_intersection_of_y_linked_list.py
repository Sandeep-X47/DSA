# Brute Force
class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

# Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to check presence of intersection
def intersectionPresent(head1, head2):
    while head2:
        temp = head1
        while temp:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    return None  # No intersection found

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing of the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")


# Better Approach
class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

# Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to check presence of intersection
def intersectionPresent(head1, head2):
    st = set()  # Set to store visited nodes from the first list
    while head1:
        st.add(head1)  # Add nodes of the first list to the set
        head1 = head1.next
    while head2:
        if head2 in st:
            return head2  # If node is found in set, it's the intersection point
        head2 = head2.next
    return None  # Return None if no intersection is found

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")


# Optimal 1
class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

# Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to get the difference in lengths of two linked lists
def getDifference(head1, head2):
    len1, len2 = 0, 0
    while head1 or head2:
        if head1:
            len1 += 1
            head1 = head1.next
        if head2:
            len2 += 1
            head2 = head2.next
    return len1 - len2  # If negative, length of list2 > length of list1, else vice-versa

# Utility function to check presence of intersection
def intersectionPresent(head1, head2):
    diff = getDifference(head1, head2)

    if diff < 0:
        while diff != 0: 
            diff += 1
            head2 = head2.next
    else:
        while diff != 0: 
            diff -= 1
            head1 = head1.next

    # Traverse both lists and compare node by node
    while head1:
        if head1 == head2:
            return head1  # Intersection point found
        head2 = head2.next
        head1 = head1.next
    return None  # No intersection found

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")


# Optimal 2
class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

# Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to check presence of intersection
def intersectionPresent(head1, head2):
    d1, d2 = head1, head2
    # Traverse both lists, when one reaches the end, redirect it to the head of the other list
    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next

    return d1  # If they meet, return the intersection node, otherwise None

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")
