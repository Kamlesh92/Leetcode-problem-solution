class Solution(object):
    def missingMultiple(self, nums, k):
        i = 1
        while True:
            if i % k == 0 and i not in nums:
                return i
            i += 1