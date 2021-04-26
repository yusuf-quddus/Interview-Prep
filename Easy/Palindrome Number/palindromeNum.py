class Solution(object):
    """
        :type x: int
        :rtype: bool
    """
    def isPalindrome(self, x):
        ints = str(x)
        end = (len(ints) - 1)
        beg = 0
        if(ints[beg] != ints[end]):
                return False
        while((beg != end) and ((beg + 1) != end)):
            end -= 1
            beg += 1
            if(ints[beg] != ints[end]):
                return False
        return True
            
      