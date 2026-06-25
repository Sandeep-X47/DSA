# Brute Force Approach
class Solution:
    def longestC(self, arr, num):
        for i in range(len(arr)):
            if arr[i] == num:
                return True
        return False
    
    def longestConsecutive(self, arr):
        longest = 1

        for i in range(len(arr)):
            count = 1

            while self.longestC(arr, arr[i] + 1):
                count += 1
                arr[i] += 1

            longest = max(longest, count)    
        return longest


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.longestConsecutive(arr))


# Better Approach
class Solution:
    def longestConsecutive(self, arr):
        Longest = 1
        arr.sort()
        count = 1

        for i in range(1, len(arr)):

            if arr[i] == arr[i - 1] + 1:
                count += 1
            elif arr[i] == arr[i - 1]:
                continue
            else:
                Longest = max(Longest, count)
                count = 1

        return max(Longest, count)


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.longestConsecutive(arr))


# Optimal Approach
class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        # If the array is empty
        if n == 0:
            return 0 

        # Initialize the longest sequence length
        longest = 1 
        st = set()

        # Put all the array elements into the set
        for i in range(n):
            st.add(nums[i])

        # Traverse the set to find the longest sequence
        for it in st:
            # Check if 'it' is a starting number of a sequence
            if it - 1 not in st:
                # Initialize the count of the current sequence
                cnt = 1 
                # Starting element of the sequence
                x = it 

                # Find consecutive numbers in the set
                while x + 1 in st:
                    # Move to the next element in the sequence
                    x = x + 1 
                    # Increment the count of the sequence
                    cnt = cnt + 1 
                # Update the longest sequence length
                longest = max(longest, cnt)
        return longest

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2] 
    # Create an instance of the solution class
    solution = Solution() 
    # Function call to find the longest consecutive sequence
    ans = solution.longestConsecutive(a) 
    print("The longest consecutive sequence is", ans)
