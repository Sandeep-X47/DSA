# Brute Force Solution
class Solution:
    def longestSubarraySumZero(self, arr):
        max_len = 0
        for i in range(len(arr)):
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]
                if curr_sum == 0:
                    max_len = max(max_len, j - i + 1)
        return max_len


if __name__ == "__main__":
    arr = [9,-3, 3, 1, 1, -3, 2, 1, 1, -3, 3, -2]

    obj = Solution()
    print(obj.longestSubarraySumZero(arr))


# Optimized Solution
class Solution:
    def longestSubarraySumZero(self, arr):

        d = {0: -1}
        max_len = 0
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum in d:
                max_len = max(max_len, i - d[curr_sum])
            else:
                d[curr_sum] = i
        return max_len        


if __name__ == "__main__":
    arr = [9,-3, 3, 1, 1, -3, 2, 1, 1, -3, 3, -2]

    obj = Solution()
    print(obj.longestSubarraySumZero(arr))