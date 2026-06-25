# Brute Force
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = 0
        a = 0
        h = len(nums1)
        b = len(nums2)
        temp = []
        while l < h and a < b:
            if nums1[l] <= nums2[a]:
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[a])
                a += 1

        while l < h:
            temp.append(nums1[l])  # Corrected this line
            l += 1

        while a < b:
            temp.append(nums2[a])  # Corrected this line
            a += 1

        if len(temp) % 2 == 0:
            z = (temp[len(temp) // 2] + temp[(len(temp) // 2) - 1]) / 2  # Corrected this line to use integer division
            return z
        else:
            return temp[len(temp) // 2] 


# Optimal Solution
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n else nums2[cut2]

            # Correct partition found
            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 0:
                    return (
                        max(left1, left2) +
                        min(right1, right2)
                    ) / 2

                return max(left1, left2)

            elif left1 > right2:
                high = cut1 - 1

            else:
                low = cut1 + 1 