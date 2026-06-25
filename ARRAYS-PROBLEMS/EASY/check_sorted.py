class Solution:
    def isSorted(self, arr):
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.isSorted(arr))