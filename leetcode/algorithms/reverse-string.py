import math

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        
        for i in range(0, l - 1):
            if i == math.floor(l/2):
                break
            x = s[i]
            y = s[l-i-1]
            
            s[i] = y
            s[l-i-1] = x
            
        return s