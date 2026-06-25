# Brute Force Approach
class Solution:
    # Function to find quadruplets with sum = target
    def fourSum(self, arr, target):
        # Get size of array
        n = len(arr)
        # Use set to store unique quadruplets
        st = set()

        # First loop - pick first element
        for i in range(n):
            # Second loop - pick second element
            for j in range(i + 1, n):
                # Third loop - pick third element
                for k in range(j + 1, n):
                    # Fourth loop - pick fourth element
                    for l in range(k + 1, n):
                        # If sum equals target
                        if arr[i] + arr[j] + arr[k] + arr[l] == target:
                            # Store sorted quadruplet as tuple
                            temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                            st.add(temp)

        # Convert set to list of lists
        return [list(quad) for quad in st]


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
ans = obj.fourSum(arr, target)
print(ans)


# Better Approach
class Solution:
    # Function to find all unique quadruplets
    def fourSum(self, arr, target):
        n = len(arr)
        st = set()  # To keep unique quadruplets

        # First loop - pick first number
        for i in range(n):
            # Second loop - pick second number
            for j in range(i + 1, n):
                seen = set()  # Store numbers between j and k

                # Third loop - pick third number
                for k in range(j + 1, n):
                    # Find required fourth number
                    required = target - arr[i] - arr[j] - arr[k]

                    # If found in seen → valid quadruplet
                    if required in seen:
                        temp = tuple(sorted([arr[i], arr[j], arr[k], required]))
                        st.add(temp)

                    # Add current number to seen
                    seen.add(arr[k])

        # Convert set to list of lists
        return [list(quad) for quad in st]


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
ans = obj.fourSum(arr, target)
print(ans)


# Optimal Approach
class Solution:
    # Function to find all unique quadruplets
    def fourSum(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []

        # Step 1: First loop for first number
        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Step 2: Second loop for second number
            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                # Step 3: Two pointers
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
print(obj.fourSum(arr, target))
