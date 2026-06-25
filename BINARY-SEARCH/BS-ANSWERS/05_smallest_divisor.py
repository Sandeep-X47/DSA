import math

# Brute Force Approach
class Solution:
    def smallestDivisor(self, arr, limit):
        n = len(arr)

        # Find the maximum element in the array
        max_val = max(arr)

        # Try all possible divisors from 1 to max_val
        for d in range(1, max_val + 1):
            total = 0
            for num in arr:
                # Divide each number by d and round up
                total += math.ceil(num / d)
            
            # If the total sum is within the limit, return this divisor
            if total <= limit:
                return d

        return -1  # If no such divisor found

# Driver code
arr = [1, 2, 3, 4, 5]
limit = 8
obj = Solution()
ans = obj.smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)


# Optimal Approach
class SmallestDivisorFinder:
    # Helper method to calculate sum by divisor
    def sumByD(self, arr, div):
        return sum(math.ceil(x / div) for x in arr)

    # Method to find the smallest divisor using binary search
    def smallestDivisor(self, arr, limit):
        if len(arr) > limit:
            return -1

        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(arr, mid) <= limit:
                high = mid - 1  # Try smaller divisor
            else:
                low = mid + 1   # Try larger divisor

        return low

# Driver code
solver = SmallestDivisorFinder()
arr = [1, 2, 3, 4, 5]
limit = 8
print("The minimum divisor is:", solver.smallestDivisor(arr, limit))
