# Extended from the previous problem of finding the maximum sum of a subarray, this problem requires us to print the subarray itself that has the maximum sum.
class Solution:
    def printMaxSubArray(self, arr):
        n = len(arr)
        max_sum = float('-inf')
        current_sum = 0

        ans_start = -1
        ans_end = -1

        for i in range(n):
            current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum
                ans_start = 0
                ans_end = i

            if current_sum < 0:
                current_sum = 0
                ans_start = i + 1

        return arr[ans_start:ans_end + 1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.printMaxSubArray(arr))


    