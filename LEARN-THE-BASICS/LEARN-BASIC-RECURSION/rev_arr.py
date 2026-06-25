# rev_arr.py
# Recursive Approach
class Solution:

    def reverse_array(self, arr: list[int], left: int, right: int) -> None:

        # Base Case
        if left >= right:
            return

        # Swap
        arr[left], arr[right] = arr[right], arr[left]

        # Recursive Call
        self.reverse_array(arr, left + 1, right - 1)


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    obj = Solution()

    obj.reverse_array(arr, 0, len(arr) - 1)

    print(arr)

# Loop Approach    
class Solution:

    def reverse_array(self, arr: list[int]) -> list[int]:
        left, right = 0, len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    obj = Solution()

    print(obj.reverse_array(arr))

# Built-in Function Approach  
class Solution:

    def reverse_array(self, arr: list[int]) -> list[int]:
        arr.reverse()
        # or arr = arr[::-1]

        return arr


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    obj = Solution()

    print(obj.reverse_array(arr))

# Brute Force Loop Approach    
class Solution:

    def reverse_array(self, arr: list[int]) -> list[int]:
        n = len(arr)
        temp = [0] * n
        for i in range(n):
            temp[i] = arr[n - 1 - i]

        return temp


if __name__ == "__main__":

    arr = list(map(int, input().split()))

    obj = Solution()

    print(obj.reverse_array(arr))    