class Solution:
    def mergeSort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2

            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)

            self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        left = arr[low : mid + 1]
        right = arr[mid + 1 : high + 1]

        i = j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
if __name__ == "__main__":
    arr = [10, 5, 2, 9, 7]

    obj = Solution()
    obj.mergeSort(arr, 0, len(arr) - 1)

    print(arr)