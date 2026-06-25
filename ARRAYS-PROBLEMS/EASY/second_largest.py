class Solution:
    def secondLargest(self, arr):
        if len(arr) < 2:
            return None

        first = second = float('-inf')
       
        for num in arr:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num

        return second if second != float('-inf') else None


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.secondLargest(arr))