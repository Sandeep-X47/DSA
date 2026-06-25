class Solution:
    def maxConsecutiveOnes(self, arr):
        count = 0
        max_count = 0
        for num in arr:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.maxConsecutiveOnes(arr))