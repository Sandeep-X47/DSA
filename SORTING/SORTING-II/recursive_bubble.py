class Solution:
    def recursiveBubbleSort(self, arr, a, n):
        if a == 0:
            return

        for i in range(a):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        self.recursiveBubbleSort(arr, a - 1, n)


if __name__ == "__main__":
    arr = [31, 27, 16, 19, 23]

    obj = Solution()
    obj.recursiveBubbleSort(arr, len(arr)-1, len(arr))

    print(arr)