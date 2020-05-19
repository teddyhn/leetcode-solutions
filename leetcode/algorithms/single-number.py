class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        
        for x in nums:
            if counts.get(x) is None:
                counts[x] = 1
            else:
                counts[x] += 1
        
        for x in counts:
            if counts[x] == 1:
                return x