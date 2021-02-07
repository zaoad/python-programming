from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        posSum=0
        negSum=0
        maxSum=0
        for num in nums:
            posSum=max(num,posSum+num)
            negSum=min(num,negSum+num)
            maxSum=max(maxSum,posSum,abs(negSum))
        return maxSum

if __name__=='__main__':
    ans=Solution().maxAbsoluteSum([-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9])
    print(ans)