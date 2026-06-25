# Brute Force Solution
class LowerBoundFinder:
    # Method to find lower bound index
    def lower_bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i] >= x:
                return i  # First index where element >= x
        return len(arr)  # If x is greater than all elements

# Driver code
arr = [3, 5, 8, 15, 19]
x = 9

finder = LowerBoundFinder()
ind = finder.lower_bound(arr, x)

print("The lower bound is the index:", ind)


# Binary Search Solution
class LowerBoundFinder:
    # Function to find the lower bound index using binary search
    def lower_bound(self, arr, x):
        low, high = 0, len(arr) - 1     # Search range
        ans = len(arr)                  # Default value if not found

        while low <= high:
            mid = (low + high) // 2     # Find middle index
            if arr[mid] >= x:
                ans = mid               # Store possible answer
                high = mid - 1          # Move to the left
            else:
                low = mid + 1           # Move to the right
        return ans                      # Return result

# Driver code
arr = [3, 5, 8, 15, 19]                # Sorted input array
x = 9                                  # Target value

finder = LowerBoundFinder()           # Create object
ind = finder.lower_bound(arr, x)      # Call method

print("The lower bound is the index:", ind)  # Output result
