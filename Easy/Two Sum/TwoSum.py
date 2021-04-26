class Solution(object):
    def twoSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
        for ints in nums:
            index = nums.index(ints) + 1
            while(index <= len(nums)-1):
                if((ints + nums[index]) == target):
                    return [nums.index(ints), index]
                index+=1
                