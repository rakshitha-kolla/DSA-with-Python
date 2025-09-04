class Solution:
    def inversionCount(self, arr):
        return self.mergesort(arr, 0, len(arr)-1)

    def mergesort(self, arr, low, high):
        count = 0
        if low < high:
            mid = (low + high) // 2
            count += self.mergesort(arr, low, mid)
            count += self.mergesort(arr, mid+1, high)
            count += self.merge(arr, low, mid, high)
        return count

    def merge(self, arr, low, mid, high):
        left = low
        right = mid + 1
        temp = []
        count = 0

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)   # inversion count
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy back to arr
        for i in range(len(temp)):
            arr[low + i] = temp[i]

        return count

s=Solution()
print(s.inversionCount([2, 4, 1, 3, 5]))  # Output: 3