# 2 loops
class Solution:
    def missingNumber(self, arr):
        for i in range(len(arr)):
            flag = 0
            for j in range(len(arr)):
                if arr[j] == i:
                    flag = 1
            if flag == 0:
                return i    
        return -1                        

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.missingNumber(arr))


# Using Hash Map
class Solution:
    def missingNumber(self, arr):
        map = {}

        for i in range(len(arr)):
            map[arr[i]] = 1

        for i in range(len(arr)):
            if i not in map:
                return i
            
        return -1            


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.missingNumber(arr)) 


# Using Sum Formula
class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        sum1, sum2 = 0, 0
        sum1 = (n * (n + 1)) // 2

        for i in range(n):
            sum2 += arr[i]

        return sum1 - sum2


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.missingNumber(arr))   


# Using XOR
class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        xor1, xor2 = 0, 0

        for i in range(n):
            xor1 ^= arr[i]

        for i in range(n + 1):
            xor2 ^= i

        return xor1 ^ xor2


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.missingNumber(arr))