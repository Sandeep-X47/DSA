# Brute Force Approach 
class Solution:
    def sort012(self, arr):
        count0 = count1 = count2 = 0

        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        for i in range(count0):
            arr[i] = 0
        for i in range(count0, count0 + count1):
            arr[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2):
            arr[i] = 2

        return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.sort012(arr))


# Optimized Approach
class Solution:
    def sort012(self, arr):
        low , mid , high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr                

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.sort012(arr))     