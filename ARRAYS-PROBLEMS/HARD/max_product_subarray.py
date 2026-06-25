# Brute Force Solution
class Solution:
    # This function finds the maximum product
    # of any contiguous subarray using brute force
    def maxProduct(self, nums):
        # Initialize the answer with the first element
        maxProd = nums[0]

        # Outer loop picks the starting index
        for i in range(len(nums)):
            # Initialize current product to 1
            prod = 1

            # Inner loop picks the ending index
            for j in range(i, len(nums)):
                # Multiply current number to product
                prod *= nums[j]

                # Update maximum product if needed
                maxProd = max(maxProd, prod)

        # Return the result
        return maxProd

# Sample input
nums = [2, 3, -2, 4]

# Create Solution object
sol = Solution()

# Print the result
print(sol.maxProduct(nums))


# Optimized Solution 1
class Solution:
    def maxProductSubArray(self, arr):
        # Store length of array
        n = len(arr)

        # Initialize prefix and suffix products
        pre, suff = 1, 1

        # Initialize answer as negative infinity
        ans = float('-inf')

        # Traverse from both front and back
        for i in range(n):
            # Reset prefix if zero
            if pre == 0:
                pre = 1

            # Reset suffix if zero
            if suff == 0:
                suff = 1

            # Multiply prefix with front element
            pre *= arr[i]

            # Multiply suffix with back element
            suff *= arr[n - i - 1]

            # Update maximum product so far
            ans = max(ans, pre, suff)

        # Return the result
        return ans

# Sample usage
arr = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProductSubArray(arr))


# Optimized Solution 2
class Solution:
    # This function returns the maximum product
    # of any contiguous subarray using optimized approach
    def maxProduct(self, nums):
        res = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        # Traverse from second element
        for i in range(1, len(nums)):
            curr = nums[i]

            # Swap max and min if current is negative
            if curr < 0:
                maxProd, minProd = minProd, maxProd

            # Update max and min product
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            # Update result
            res = max(res, maxProd)

        return res

nums = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProduct(nums))
