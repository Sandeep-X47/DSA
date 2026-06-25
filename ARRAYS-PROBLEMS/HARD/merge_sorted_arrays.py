class Solution:
    def mergeSortedArrays(self, arr1, arr2, m, n):
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1

        return arr1


if __name__ == "__main__":
    nums1 = [1, 3, 5, 0, 0, 0]
    nums2 = [2, 4, 6]
    m, n = 3, 3
    obj = Solution()
    print(obj.mergeSortedArrays(nums1, nums2, m, n))