class Solution:
    def maxSubArray(self, nums):
        curr=best=nums[0]
        for i in nums[1:]:
            curr=max(i,curr+i)
            best=max(best,curr)
        return best

res=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(res.maxSubArray(nums))


"""

output:  6

The maximum subarray is [4,-1,2,1] with sum 6.

"""
