from typing import List

class Solution:
    # Function to merge overlapping intervals using brute force
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals based on the start time
        intervals.sort()

        ans = []
        n = len(intervals)
        i = 0

        # Loop through each interval
        while i < n:
            # Take current interval's start and end
            start = intervals[i][0]
            end = intervals[i][1]

            j = i + 1

            # Merge with all intervals that overlap
            while j < n and intervals[j][0] <= end:
                # Extend the end if overlapping
                end = max(end, intervals[j][1])
                j += 1

            # Append merged interval to result
            ans.append([start, end])

            # Move to the next non-overlapping interval
            i = j

        return ans

# Driver code
sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))


# Optimal approach 
class Solution:
    # Function to merge overlapping intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort()

        # List to store final merged intervals
        merged = []

        # Traverse all intervals
        for interval in intervals:
            # If merged list is empty or current interval doesn't overlap
            if not merged or merged[-1][1] < interval[0]:
                # Append current interval as a new one
                merged.append(interval)
            else:
                # Overlapping: merge by extending the end
                merged[-1][1] = max(
                    merged[-1][1],
                    interval[1]
                )

        return merged

# Example usage
sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(intervals))
