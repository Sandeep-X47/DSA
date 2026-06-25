class Solution:
    def findPairsWithGivenSum(self, target, head):
        
        # left pointer at head
        left = head
        
        # right pointer at tail
        right = head
        while right.next:
            right = right.next
        
        ans = []
        
        # two pointer search
        while left != right and left.prev != right:
            
            s = left.data + right.data
            
            if s == target:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev
            
            elif s < target:
                left = left.next
            
            else:
                right = right.prev
        
        return ans