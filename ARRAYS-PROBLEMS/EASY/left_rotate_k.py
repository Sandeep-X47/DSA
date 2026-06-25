class Solution:
    def leftRotateK(self, arr, k):
        if not arr or k == 0:
            return arr

        n = len(arr)
        k = k % n  # Handle cases where k is larger than the array length

        # Reverse the first k elements
        arr[:k] = reversed(arr[:k])
        # Reverse the remaining elements
        arr[n-k-1:] = reversed(arr[n-k-1:])
        # Reverse the entire array
        arr.reverse()
        return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = int(input())

    obj = Solution()
    print(obj.leftRotateK(arr, k))
    print() 
    
class Solution:
    def rightRotateK(self, arr, k):
        if not arr or k == 0:
            return arr

        n = len(arr)
        k = k % n  # Handle cases where k is larger than the array length

        # Reverse the entire array
        arr.reverse()
        # Reverse the first k elements
        arr[:k] = reversed(arr[:k])
        # Reverse the remaining elements
        arr[n-k-1:] = reversed(arr[n-k-1:])
        
        return arr
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = int(input())

    obj = Solution()
    print(obj.rightRotateK(arr, k))        
