# Brute Force Solution
class Solution:
    def longestSubarraySumK(self, arr, k):
        n = len(arr)
        max_length = 0
        current_sum = 0
        for i in range(n):
            for j in range(i, n):
                current_sum += arr[j]
                if current_sum == k:
                    max_length = max(max_length, j - i + 1)
                    break
                elif current_sum > k:
                    break                    
        return max_length


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    obj = Solution()
    print(obj.longestSubarraySumK(arr, k))


# Optimized Solution   
class Solution:
    def longestSubarraySumK(self, arr, k):
        n = len(arr)
        max_length = 0
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > k and left <= right:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == k:
                max_length = max(max_length, right - left + 1)
        
        return max_length


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    obj = Solution()
    print(obj.longestSubarraySumK(arr, k)) 