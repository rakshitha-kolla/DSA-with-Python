class Solution:
    def intersection(self, arr1, arr2):
        # code here
        inter = []
        i = 0
        j = 0
        while (i < len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr1[i]:
                j += 1
            else:
                if not inter or inter[-1] != arr1[i]:
                    inter.append(arr1[i])
                i += 1
                j += 1
        return inter


s=Solution()
print(s.intersection([1, 2, 3, 4],[2, 4, 6, 7, 8]))