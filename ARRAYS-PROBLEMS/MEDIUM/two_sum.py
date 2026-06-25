# Brute Force Approach
class Solution:
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return (i, j)
        return None


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    obj = Solution()
    print(obj.twoSum(arr, target))


# Hash Map Solution
class Solution:
    def twoSum(self, arr, target):
        num_dict = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return None


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    obj = Solution()
    print(obj.twoSum(arr, target))


# Optimized Solution
class Solution:
    def twoSum(self, arr, target):
        two_sum = []
        left, right = 0, len(arr) - 1

        for idx, num in enumerate(arr):
            two_sum.append((num, idx))

        while left < right:
            current_sum = two_sum[left][0] + two_sum[right][0]
            if current_sum == target:
                return (two_sum[left][1], two_sum[right][1])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                            
        return None

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    obj = Solution()
    print(obj.twoSum(arr, target))    