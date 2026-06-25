class Solution:
    def leftRotateOne(self, arr):
        if not arr:
            return arr
        first = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = first
        return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    obj = Solution()
    print(obj.leftRotateOne(arr))