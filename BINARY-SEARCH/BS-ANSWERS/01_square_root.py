# Brute Force Approach
class Solution:
    # Function to find floor of square root using linear search
    def floorSqrt(self, n: int) -> int:

        if n < 2:
            return n
        
        # Variable to store answer
        ans = 0

        # Run loop from 1 to n
        for i in range(1, n + 1):
            # Check if i*i <= n
            if i * i <= n:
                # Update answer
                ans = i
            else:
                # Break when i*i > n
                break

        # Return final answer
        return ans


# Example input
n = 27

# Create object of Solution
sol = Solution()

# Call function and print result
print(sol.floorSqrt(n))


# Binary Search Approach
class Solution:
    # This function returns the floor value of the square root of a number
    def mySqrt(self, x: int) -> int:
        # Handle small numbers directly
        if x < 2:
            return x

        # Initialize binary search range
        left, right, ans = 1, x // 2, 0

        # Perform binary search
        while left <= right:
            # Find middle point
            mid = (left + right) // 2

            # Check if mid*mid is less than or equal to x
            if mid * mid <= x:
                # Store mid as potential answer
                ans = mid
                # Move to right half
                left = mid + 1
            else:
                # Move to left half
                right = mid - 1

        # Return final answer
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))
