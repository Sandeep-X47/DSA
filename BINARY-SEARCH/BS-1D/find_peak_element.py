# Brute Force Approach
class Solution:
    # Function to find a peak element in the array
    def findPeakElement(self, nums):
        n = len(nums)

        # Traverse the array
        for i in range(n):
            # Check left neighbor if exists
            left = (i == 0) or (nums[i] >= nums[i - 1])
            # Check right neighbor if exists
            right = (i == n - 1) or (nums[i] >= nums[i + 1])

            # If both conditions are true
            if left and right:
                return i

        # In case no peak found
        return -1

# Driver
sol = Solution()
nums = [1, 3, 20, 4, 1, 0]
index = sol.findPeakElement(nums)
print(f"Peak at index: {index} with value: {nums[index]}")


# Optimal Approach (Binary Search)
class Solution:
    # Function to find a peak element using binary search
    def findPeakElement(self, nums):
        # Set left and right bounds
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:
            # Find mid point
            mid = (low + high) // 2

            # If mid element is greater than next
            if nums[mid] > nums[mid + 1]:
                # Move to left half
                high = mid
            else:
                # Move to right half
                low = mid + 1

        # Return peak index
        return low

# Input array
nums = [1, 2, 1, 3, 5, 6, 4]

# Create object
obj = Solution()

# Output result
print(obj.findPeakElement(nums))
