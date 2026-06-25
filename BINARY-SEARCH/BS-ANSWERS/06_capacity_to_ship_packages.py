# Brute Force
class Solution:
    # Function to check how many days needed for given capacity
    def daysNeeded(self, weights, capacity):
        # Initialize day count to 1
        days = 1
        # Current load for the day
        currentLoad = 0

        # Iterate over all package weights
        for w in weights:
            # If adding weight exceeds capacity
            if currentLoad + w > capacity:
                # Increase day count and reset load
                days += 1
                currentLoad = w
            else:
                # Otherwise, add weight to current load
                currentLoad += w
        # Return total days needed
        return days

    # Function to find minimum ship capacity to ship in d days
    def shipWithinDays(self, weights, d):
        # Find maximum weight as minimum capacity
        left = max(weights)
        # Find total sum as maximum capacity
        right = sum(weights)

        # Iterate from minimum to maximum capacity
        for capacity in range(left, right + 1):
            # Calculate days needed for current capacity
            needed = self.daysNeeded(weights, capacity)
            # If days needed are less than or equal to d, return capacity
            if needed <= d:
                return capacity
        # Should never reach here given constraints
        return right


if __name__ == "__main__":
    # Input weights
    weights = [5,4,5,2,3,4,5,6]
    # Days to ship
    d = 5
    # Create Solution instance
    sol = Solution()
    # Call the function and print result
    print(sol.shipWithinDays(weights, d))


# Optimal Approach
class Solution:
    # Function to calculate how many days are needed to ship
    # all packages with the given ship capacity
    def daysNeeded(self, weights, capacity):
        # Initialize count of days to 1
        days = 1
        # Initialize current load on ship to 0
        currentLoad = 0

        # Iterate over all package weights
        for w in weights:
            # Check if adding current package exceeds capacity
            if currentLoad + w > capacity:
                # If yes, increase days count since we start a new day
                days += 1
                # Reset current load to current package weight
                currentLoad = w
            else:
                # Else, add current package weight to current load
                currentLoad += w
        # Return total days required
        return days

    # Function to find minimum ship capacity to ship all packages within d days
    def shipWithinDays(self, weights, d):
        # Calculate minimum capacity as max weight in packages
        left = max(weights)
        # Calculate maximum capacity as sum of all weights
        right = sum(weights)

        # Binary search between left and right capacity values
        while left < right:
            # Calculate mid value to test
            mid = left + (right - left) // 2
            # Calculate how many days needed for capacity mid
            needed = self.daysNeeded(weights, mid)

            # If days needed is less or equal to allowed days,
            # try to find smaller capacity on left side
            if needed <= d:
                right = mid
            else:
                # Else, need more capacity, search on right side
                left = mid + 1

        # Return minimum capacity found
        return left


if __name__ == "__main__":
    # Define array of package weights
    weights = [5,4,5,2,3,4,5,6]
    # Define number of days allowed for shipping
    d = 5
    # Create Solution object
    sol = Solution()
    # Print minimum capacity required to ship within d days
    print(sol.shipWithinDays(weights, d))
