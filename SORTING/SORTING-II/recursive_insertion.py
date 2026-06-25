class Solution:
    def recursiveInsertionSort(self, arr, a, n):
        if a >= n:
            return

        key = arr[a]
        j = a - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        self.recursiveInsertionSort(arr, a + 1, n)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    obj = Solution()
    obj.recursiveInsertionSort(arr, 1, len(arr))
    print(arr)