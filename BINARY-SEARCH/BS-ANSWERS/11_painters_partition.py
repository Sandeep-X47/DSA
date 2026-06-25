# Brute Force 
from typing import List

class PainterPartition:
    # Helper to count how many painters are required for a given max time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1              # Start with one painter
        boards_painter = 0        # Current load on a painter

        for board in boards:
            if boards_painter + board <= time:
                # Assign board to the current painter
                boards_painter += board
            else:
                # Assign board to a new painter
                painters += 1
                boards_painter = board

        return painters

    # Function to find the minimum maximum time to paint all boards with k painters
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)         # No painter can paint less than the largest board
        high = sum(boards)        # All boards painted by one painter (max possible)

        for time in range(low, high + 1):
            if self.count_painters(boards, time) <= k:
                return time       # Found a valid configuration

        return low  # Fallback case

# Test case
boards = [10, 20, 30, 40]
k = 2

pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)

print("The answer is:", ans)  # Expected: 60


# Optimal Approach
from typing import List

class PainterPartition:
    # Count painters required for a given max allowed time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    # Use binary search to find the minimum time
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        result = high

        while low <= high:
            mid = (low + high) // 2
            painters = self.count_painters(boards, mid)

            if painters > k:
                low = mid + 1  # Too few painters, increase time
            else:
                result = mid   # Valid time, try reducing it
                high = mid - 1

        return result

# Test
boards = [10, 20, 30, 40]
k = 2
pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)
print("The answer is:", ans)  # Expected: 60
