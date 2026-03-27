class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        for i in range(0,l):
            if target == nums[i]:
                return i
            elif (nums[i] < target) and ( (i+1)>l-1 ):
                return i+1
            elif (nums[i] < target) and (nums[i+1]>target):
                return i+1
        return 0