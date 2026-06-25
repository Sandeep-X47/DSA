import math

# Brute Force Approach
class Solution:

    def count_digits(self, n: int) -> int:
        N = n
        cnt = 0
        while N > 0:
            N = N // 10
            cnt += 1
        return cnt


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.count_digits(n))

# Optimal Approach   
class Solution:

    def count_digits(self, n: int) -> int:
        cnt = int(math.log10(n) + 1)
        return cnt

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.count_digits(n))
 
