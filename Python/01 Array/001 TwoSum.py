class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        table = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in table:
                return table[remain], i
            table[nums[i]] = i
        return None