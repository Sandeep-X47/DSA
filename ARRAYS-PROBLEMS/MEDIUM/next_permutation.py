from itertools import permutations

# Brute Force
class Solution:
    # Function to find the next permutation
    def nextPermutation(self, nums):
        # Generate all unique permutations
        perms = sorted(set(permutations(nums)))

        # Convert list to tuple for comparison
        current = tuple(nums)

        # Traverse the list
        for i in range(len(perms)):
            if perms[i] == current:
                # If last permutation, return first
                if i == len(perms) - 1:
                    return list(perms[0])
                # Else return next
                return list(perms[i + 1])

        return nums

# Driver code
sol = Solution()
nums = [1, 2, 3]
result = sol.nextPermutation(nums)
print(" ".join(map(str, result)))


# Optimal Solution
class Solution:
    # Function to find next permutation
    def nextPermutation(self, nums):
        # Set index
        index = -1

        # Find decreasing point
        for i in range(len(nums) - 2, -1, -1):
            # If smaller found
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no such index
        if index == -1:
            # Reverse whole list
            nums.reverse()
            return

        # Find just greater element
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                # Swap them
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse part after index
        nums[index + 1:] = reversed(nums[index + 1:])

# Main driver
def main():
    # Input list
    nums = [1, 2, 3, 6, 5, 4]

    # Create object
    sol = Solution()

    # Call function
    sol.nextPermutation(nums)

    # Print result
    print(" ".join(map(str, nums)))

# Run main
main()
