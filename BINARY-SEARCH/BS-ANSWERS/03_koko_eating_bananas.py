import math

# Brute Force Approach
class Solution:
    # Function to calculate total hours for given speed
    def calculateTotalHours(self, a, hourly):
        totalHours = 0
        for pile in a:
            # Add hours using ceil
            totalHours += math.ceil(pile / hourly)
        return totalHours

    # Function to find minimum eating speed
    def minEatingSpeed(self, a, h):
        # Find maximum pile size
        maxVal = max(a)

        # Try every possible speed
        for i in range(1, maxVal + 1):
            hours = self.calculateTotalHours(a, i)

            # If hours fit within h
            if hours <= h:
                return i
        return maxVal

# Driver code
a = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(a, h))


# Optimal Approach using Binary Search
class Solution:
    # Function to calculate total hours at given speed
    def calculateTotalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    # Function to find minimum eating speed
    def minEatingSpeed(self, piles, h):
        # Find maximum element
        maxPile = max(piles)

        # Initialize low and high pointers
        low, high = 1, maxPile
        ans = maxPile

        # Binary search on answer space
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)

            # If possible, try smaller speed
            if totalH <= h:
                ans = mid
                high = mid - 1
            # Otherwise, try larger speed
            else:
                low = mid + 1

        return ans

# Driver code
piles = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))
