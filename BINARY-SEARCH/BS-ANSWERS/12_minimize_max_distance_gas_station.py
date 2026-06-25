# Brute Force 
class GasStationSolver:
    def minimise_max_distance(self, arr, k):
        n = len(arr)
        how_many = [0] * (n - 1)  # Extra stations between each pair

        # Place k gas stations
        for _ in range(k):
            max_section = -1
            max_ind = -1

            # Find segment with maximum section length
            for i in range(n - 1):
                diff = arr[i + 1] - arr[i]
                section_length = diff / (how_many[i] + 1)
                if section_length > max_section:
                    max_section = section_length
                    max_ind = i

            # Add one gas station to the longest section
            how_many[max_ind] += 1

        # Calculate final maximum section length
        max_ans = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            section_length = diff / (how_many[i] + 1)
            max_ans = max(max_ans, section_length)

        return max_ans

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
solver = GasStationSolver()
ans = solver.minimise_max_distance(arr, k)
print("The answer is:", ans)


# Better Approach
import heapq

class Solution:
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)
        howMany = [0] * (n - 1)

        # Max-heap using negative values
        pq = []
        for i in range(n - 1):
            dist = arr[i + 1] - arr[i]
            heapq.heappush(pq, (-dist, i))  # Use negative for max-heap

        for _ in range(k):
            negDist, idx = heapq.heappop(pq)
            howMany[idx] += 1

            totalDist = arr[idx + 1] - arr[idx]
            newDist = totalDist / (howMany[idx] + 1)
            heapq.heappush(pq, (-newDist, idx))

        # Return the max distance (negated back)
        return -pq[0][0]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
sol = Solution()
print("The answer is:", sol.minimiseMaxDistance(arr, k))


# Optimal Approach
class GasStationOptimizer:
    # Function to calculate how many gas stations are needed 
    # if the maximum allowed distance between stations is 'dist'
    def number_of_gas_stations_required(self, dist, arr):
        count = 0  # total number of additional gas stations required
        n = len(arr)

        # Iterate through consecutive station positions
        for i in range(1, n):
            # Calculate how many stations are needed between arr[i-1] and arr[i]
            number_in_between = int((arr[i] - arr[i - 1]) / dist)

            # If the distance divides perfectly, we overcounted by 1,
            # so subtract one extra station
            if (arr[i] - arr[i - 1]) == dist * number_in_between:
                number_in_between -= 1

            count += number_in_between  # accumulate required stations

        return count  # return total number of extra stations needed

    # Function to minimize the maximum distance between gas stations
    def minimise_max_distance(self, arr, k):
        # Binary search between smallest (0) and largest gap in stations
        low = 0
        high = max(arr[i+1] - arr[i] for i in range(len(arr) - 1))

        diff = 1e-6  # precision tolerance for stopping condition

        # Binary search loop until precision is achieved
        while high - low > diff:
            mid = (low + high) / 2.0  # candidate distance
            count = self.number_of_gas_stations_required(mid, arr)

            # If more than k stations are required, increase distance
            if count > k:
                low = mid
            else:
                # Otherwise we can reduce the distance
                high = mid

        return high  # minimum possible maximum distance

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # positions of existing gas stations
    k = 4  # number of additional gas stations allowed

    optimizer = GasStationOptimizer()
    result = optimizer.minimise_max_distance(arr, k)

    print("The answer is:", result)

