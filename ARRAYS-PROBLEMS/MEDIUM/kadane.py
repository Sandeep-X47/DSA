# Brute force approach: O(n^2)
class Solution:
    def maxSubArray(self, arr):
        n = len(arr)
        max_sum = float("-inf")
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    obj = Solution()
    print(obj.maxSubArray(arr))


# Optimal approach: O(n)
class Solution:
    def maxSubArray(self, arr):
        n = len(arr)
        max_sum = float("-inf")
        current_sum = 0

        for i in range(n):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)

        return max_sum 

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    obj = Solution()
    print(obj.maxSubArray(arr))

