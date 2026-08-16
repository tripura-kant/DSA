class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        result = {}
        for i in range(n):
            if nums[i] in result:
                return True
            result[nums[i]] = 1
        return False