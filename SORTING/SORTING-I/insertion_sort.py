class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    obj = Solution()
    obj.insertionSort(arr)

    print(arr)
    