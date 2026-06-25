class Solution:
    def moveZeros(self, arr):
        if not arr:
            return arr
        zero = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                zero = i
                break
        if zero == -1:
            return arr

        for i in range(zero + 1, len(arr)):
            if arr[i] != 0:
                arr[zero] = arr[i]
                arr[i] = 0
                zero += 1
        return arr            


if __name__ == "__main__":
    arr = [0, 1, 0, 1, 2, 3, 4, 12]

    obj = Solution()
    print(obj.moveZeros(arr))

