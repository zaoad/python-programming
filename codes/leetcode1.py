from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
if __name__=='__main__':
        arr=Solution.twoSum(Solution,[0,1,2],3)
        print(arr)

