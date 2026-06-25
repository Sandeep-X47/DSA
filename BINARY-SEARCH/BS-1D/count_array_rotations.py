# Brute Force Approach
class Solution:
    # Function to find the number of rotations in a rotated sorted array
    def findRotations(self, arr):
        # Store size of array
        n = len(arr)

        # Assume the first element is the smallest
        minVal = arr[0]

        # Index of the smallest element
        minIndex = 0

        # Traverse the array
        for i in range(1, n):
            # If current element is smaller than minVal, update
            if arr[i] < minVal:
                minVal = arr[i]
                minIndex = i

        # The index of smallest element = number of rotations
        return minIndex


# Driver code
if __name__ == "__main__":
    obj = Solution()

    # Example input
    arr = [4,5,6,7,0,1,2,3]

    # Call the function and store result
    rotations = obj.findRotations(arr)

    # Print result
    print(rotations)


# Better Approach (Using Binary Search)
class Solution:
    # Function to find rotation count using one-pass scan
    def findRotationCount(self, arr):
        # Get size of array
        n = len(arr)
        # Traverse till second-last element
        for i in range(n - 1):
            # If break point found
            if arr[i] > arr[i + 1]:
                # Return index of next element as rotation count
                return i + 1
        # No rotation found
        return 0

# Driver code
if __name__ == "__main__":
    # Example input
    arr = [3, 4, 5, 1, 2]

    # Create Solution object
    sol = Solution()

    # Call the function
    rotations = sol.findRotationCount(arr)

    # Output result
    print(rotations)


# Optimal Approach (Using Binary Search)
class Solution:
    # Function to find rotation count using binary search
    def findRotations(self, arr):
        low = 0
        high = len(arr) - 1

        # Loop until low meets high
        while low < high:
            mid = low + (high - low) // 2

            # If mid element is greater than element at high,
            # smallest element lies to the right of mid
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                # Else smallest element is at mid or to the left
                high = mid

        # When low == high, we found the smallest element
        return low

# Driver code
if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2,3]
    sol = Solution()
    rotations = sol.findRotations(arr)
    print(rotations)
