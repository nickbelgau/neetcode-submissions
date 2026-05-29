class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Use two pointers from the end. 
        If you merge from the front, 
        you overwrite values in nums1 that you still need. 
        Merging from the back avoids that.
        """
        i = m - 1          # last valid element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # fill position in nums1 from the end

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1