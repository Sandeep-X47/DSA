# Brute Force Approach
class Solution:
    def singleNumber(self, arr):
        for num in arr:
            count = 0
            for i in arr:
                if num == i:
                    count += 1
            if count == 1:
                return num
        return -1


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.singleNumber(arr))


# Hash Map Approach
class Solution:
    def singleNumber(self, arr):
        map = {}
        for num in arr:
            map[num] = map.get(num, 0) + 1
        for num, count in map.items():
            if count == 1:
                return num
        return -1


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.singleNumber(arr))    


# Optimal Approach (XOR)
class Solution:
    def singleNumber(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.singleNumber(arr))