from typing import List
from collections import defaultdict

# Brute Force 
class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        # Size of the array
        n = len(nums)
        
        # List of answers
        result = []
        
        for i in range(n):
            """ Checking if nums[i] is not 
            already part of the answer """
            if len(result) == 0 or result[0] != nums[i]:
                
                cnt = 0
                
                for j in range(n):
                    # counting the frequency of nums[i]
                    if nums[j] == nums[i]:
                        cnt += 1
                
                # check if frequency is greater than n/3
                if cnt > (n // 3):
                    result.append(nums[i])
                
            # if result size is equal to 2 break out of loop
            if len(result) == 2:
                break
        
        # return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", end=" ")
    for it in ans:
        print(it, end=" ")
    print()


# Better Approach
class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        # Size of the array
        n = len(nums)

        # List of answers
        result = []

        # Declaring a map
        mpp = defaultdict(int)

        # Least occurrence of the majority element
        mini = n // 3 + 1

        # Storing the elements with its occurrence
        for num in nums:
            mpp[num] += 1

            # Checking if num is the majority element
            if mpp[num] == mini:
                result.append(num)

            # If result size is equal to 2 break out of loop
            if len(result) == 2:
                break

        # Return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", *ans)    


# Optimal Approach (Boyer-Moore Voting Algorithm)
class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        # Size of the array
        n = len(nums)

        # Counts for elements el1 and el2
        cnt1, cnt2 = 0, 0
        
        """Initialize Element 1 and 
        Element 2 with INT_MIN value"""
        el1, el2 = float('-inf'), float('-inf')

        """Find the potential candidates using
        Boyer Moore's Voting Algorithm"""
        for num in nums:
            if cnt1 == 0 and el2 != num:
                cnt1 = 1
                # Initialize el1 as num
                el1 = num 
            elif cnt2 == 0 and el1 != num:
                cnt2 = 1
                # Initialize el2 as num
                el2 = num 
            elif num == el1:
                # Increment count for el1
                cnt1 += 1
            elif num == el2:
                # Increment count for el2
                cnt2 += 1 
            else:
                # Decrement count for el1
                cnt1 -= 1 
                 # Decrement count for el2
                cnt2 -= 1

        #Validate the candidates by counting occurrences in nums
        #Reset counts for el1 and el2
        cnt1, cnt2 = 0, 0 
        
        for num in nums:
            if num == el1:
                # Count occurrences of el1
                cnt1 += 1 
            if num == el2:
                 # Count occurrences of el2
                cnt2 += 1

        """ Determine the minimum count
        required for a majority element"""
        mini = n // 3 + 1
        
        # List of answers
        result = []

        """Add elements to the result list
        if they appear more than n/3 times"""
        if cnt1 >= mini:
            result.append(el1)
            
        if cnt2 >= mini and el1 != el2:
            # Avoid adding duplicate if el1 == el2
            result.append(el2)

        # Uncomment the following line if you want to sort the answer list
        # result.sort() # TC --> O(2*log2) ~ O(1);

        #return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
  
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", *ans)