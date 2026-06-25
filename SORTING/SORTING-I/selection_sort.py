class Solution:
    def selectionSort(self, arr,n):
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    n = len(arr)
    obj = Solution()
    obj.selectionSort(arr,n)

    print(arr)
    