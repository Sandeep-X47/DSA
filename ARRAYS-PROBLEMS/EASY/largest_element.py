class Solution:
    def largestElement(self, arr):
        max_element = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_element:
                max_element = arr[i]
        return max_element


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.largestElement(arr))