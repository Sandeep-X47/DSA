# Brute Force
class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Solution:
    def pal(self, head):  

        if head is None or head.next is None :
            return True
        
        temp = head
        stk = []

        while temp:
            stk.append(temp.data)
            temp = temp.next

        temp = head
        while temp:
            if temp.data != stk.pop():    
                return False
            
            temp = temp.next

        return True            

# Driver code
if __name__ == "__main__":
    # Create linked list nodes
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    
    sol = Solution()
    if sol.pal(head):
        print("Palindrome")
    else:
        print("Not Palindrome")    
    

# Optimal
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def pal(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 3. Compare the first half and the reversed second half
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed half
        
        while second_half:  # Only need to check the second half length
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True

# Driver code
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    
    sol = Solution()
    if sol.pal(head):
        print("Palindrome")
    else:
        print("Not Palindrome")
        