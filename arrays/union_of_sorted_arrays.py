class Solution:
    def findUnion(self, a, b):
        # code here
        u = []
        i = 0
        j = 0

        while (i < len(a) and j < len(b)):
            if a[i] < b[j]:
                if not u or u[-1] != a[i]:
                    u.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if not u or u[-1] != b[j]:
                    u.append(b[j])
                j += 1
            else:
                if not u or u[-1] != a[i]:
                    u.append(a[i])
                i += 1
                j += 1

        while (i < len(a)):
            if not u or u[-1] != a[i]:
                u.append(a[i])
            i += 1
        while (j < len(b)):
            if not u or b[j] != u[-1]:
                u.append(b[j])
            j += 1
        return u
s=Solution()
print(s.findUnion([1, 2, 3, 4, 5],  [1, 2, 3, 6, 7]))