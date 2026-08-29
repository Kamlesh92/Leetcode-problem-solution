class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        result = [0] * n
        # Pair each value with its original index and sort by value
        pairs = sorted((num, i) for i, num in enumerate(nums))

        i = 0
        while i < n:
            j = i
            # Expand window for elements connected by difference <= limit
            while j + 1 < n and pairs[j+1][0] - pairs[j][0] <= limit:
                j += 1
            
            # Extract and sort the original indices occupied by this component
            indices = sorted([pairs[k][1] for k in range(i, j + 1)])
            
            # Greedily assign smallest values to the leftmost original positions
            for k, idx in enumerate(indices):
                result[idx] = pairs[i + k][0]
                
            i = j + 1
        
        return result