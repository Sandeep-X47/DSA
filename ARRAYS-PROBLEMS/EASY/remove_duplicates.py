class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        j = 0
        for i in range(1, n):
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]
        return j + 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    k =obj.removeDuplicates(arr)
    print(arr[:k])