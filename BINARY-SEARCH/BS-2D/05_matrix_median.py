# Brute Force
class Solution:
    def findMedian(self, matrix):

        # Create a list to store all elements
        elements = []

        # Traverse each row
        for row in matrix:

            # Traverse each value in the row
            for val in row:

                # Add value to list
                elements.append(val)

        # Sort all collected elements
        elements.sort()

        # Return the middle value (median)
        return elements[len(elements) // 2]

# Driver code
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

obj = Solution()
print(obj.findMedian(matrix))


# Optimal
import bisect

class Solution:
    # Function to count elements <= mid using bisect
    def countLessEqual(self, row, mid):
        return bisect.bisect_right(row, mid)

    # Function to find median
    def findMedian(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Get the smallest and largest elements
        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        # Binary search on value space
        while low < high:
            mid = (low + high) // 2
            count = 0

            # Count elements ≤ mid
            for row in matrix:
                count += self.countLessEqual(row, mid)

            if count < (rows * cols + 1) // 2:
                low = mid + 1
            else:
                high = mid

        return low

# Driver code
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
obj = Solution()
print("Median:", obj.findMedian(matrix))
