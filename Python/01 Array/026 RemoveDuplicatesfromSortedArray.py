class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        rtn = 1
        for i in nums:
            if nums[rtn-1] != i:
                nums[rtn] = i
                rtn +=1
        return rtn