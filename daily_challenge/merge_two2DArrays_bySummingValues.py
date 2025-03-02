''' Merge Two 2D Arrays by Summing Values
You are given two 2D integer arrays nums1 and nums2.
    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.



Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
'''
class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        N1, N2 = len(nums1), len(nums2)
        ptr1, ptr2 = 0, 0

        merged_array = []
        while ptr1 < N1 and ptr2 < N2:
            # If the id is same, add the values and insert to the result.
            # Increment both pointers.
            if nums1[ptr1][0] == nums2[ptr2][0]:
                merged_array.append(
                    [nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]]
                )
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                # If the id in nums1 is smaller, add it to result and increment the pointer
                merged_array.append(nums1[ptr1])
                ptr1 += 1
            else:
                # If the id in nums2 is smaller, add it to result and increment the pointer
                merged_array.append(nums2[ptr2])
                ptr2 += 1

        # If pairs are remaining in the nums1, then add them to the result.
        while ptr1 < N1:
            merged_array.append(nums1[ptr1])
            ptr1 += 1

        # If pairs are remaining in the nums2, then add them to the result.
        while ptr2 < N2:
            merged_array.append(nums2[ptr2])
            ptr2 += 1

        return merged_array
s=Solution()
print(s.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))