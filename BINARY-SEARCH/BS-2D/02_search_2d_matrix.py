# Brute Force
class Solution:
    # Function to search for a target value in the matrix
    def searchMatrix(self, matrix, target):
        # Get number of rows in the matrix
        n = len(matrix)

        # Get number of columns in the matrix
        m = len(matrix[0])

        # Traverse each row
        for i in range(n):
            # Traverse each column in the current row
            for j in range(m):
                # Check if the current element matches the target
                if matrix[i][j] == target:
                    return True

        # Return false if the target is not found
        return False

# Driver code
if __name__ == "__main__":
    # Define a 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create an object of the Solution class
    obj = Solution()

    # Call the searchMatrix function and print the result
    if obj.searchMatrix(matrix, 8):
        print("true")
    else:
        print("false")


# Better Approach
class Solution:
    # Function to perform binary search on a list
    def binarySearch(self, nums, target):
        # Get the length of the array
        n = len(nums)

        # Initialize low and high pointers
        low, high = 0, n - 1

        # Binary search loop
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2

            # If target is found at mid
            if nums[mid] == target:
                return True

            # If target is greater, search right half
            elif target > nums[mid]:
                low = mid + 1

            # Otherwise, search left half
            else:
                high = mid - 1

        # Return False if not found
        return False

    # Function to search for target in 2D matrix
    def searchMatrix(self, matrix, target):
        # Get number of rows
        n = len(matrix)

        # Get number of columns
        m = len(matrix[0])

        # Traverse each row
        for i in range(n):
            # Check if target can be in this row
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                # Perform binary search on this row
                return self.binarySearch(matrix[i], target)

        # Return False if not found
        return False

# Driver code
if __name__ == "__main__":
    # Define a 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create an object of the Solution class
    obj = Solution()

    # Call the searchMatrix method and print the result
    if obj.searchMatrix(matrix, 8):
        print("true")
    else:
        print("false")


# Optimal 
class Solution:
    # Function to search target in 2D matrix using binary search
    def searchMatrix(self, matrix, target):
        # Get number of rows and columns
        n = len(matrix)
        m = len(matrix[0])

        # Set initial binary search range
        low = 0
        high = n * m - 1

        # Perform binary search
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2

            # Convert 1D index to 2D indices
            row = mid // m
            col = mid % m

            # Check if target is found
            if matrix[row][col] == target:
                return True
            # Discard left half
            elif matrix[row][col] < target:
                low = mid + 1
            # Discard right half
            else:
                high = mid - 1

        # Target not found
        return False

# Driver code
if __name__ == "__main__":
    # Define 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create object of Solution
    obj = Solution()

    # Call the method and print result
    print("true" if obj.searchMatrix(matrix, 8) else "false")
