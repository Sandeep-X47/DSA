# Brute Force Solution
class Solution:
    def majorityElement(self, arr):
        n = len(arr)

        for i in range(n):
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1

            if count > n // 2:
                return arr[i]
            
        return -1    

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.majorityElement(arr))


# Hash Map Solution
class Solution:
    def majorityElement(self, arr):
        map = {}
        n = len(arr)

        for i in range(n):
            map[arr[i]] = map.get(arr[i], 0) + 1

        for num, count in map.items():
            if count > n // 2:
                return num

        return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.majorityElement(arr))


# Optimized Solution
class Solution:
    def majorityElement(self, arr):
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                count = 1
                candidate = num
            elif num == candidate:
                count += 1
            else:
                count -= 1        

        return candidate


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.majorityElement(arr))    