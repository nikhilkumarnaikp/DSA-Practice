
class Solution:
    def maxProduct(self,nums):
        res=minp=maxp=nums[0]
        for x in nums[1:]:
            if x==0:
                minp=maxp=1
            temp=(x,maxp*x,minp*x)
            minp=min(temp)
            maxp=max(temp)
            res=max(res,maxp)
        return res

ans=Solution()
nums=[-2,3,-2,4,-4]
print(ans.maxProduct(nums))

"""
output:  48
The maximum product subarray is [3,-2,4,-4] with product 48.
 
"""

