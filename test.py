# from typing import List
# import sys
# class Solution:
#     def twoSum(nums: List[int], target: int) -> List[int]:
#         for ni , n in enumerate(nums):
#             for ni2 , n2 in enumerate(nums):
#                 if ni2 == len(nums)-1:
#                     continue
#                 x = nums[ni2 + 1]
#                 if n + x == target:
#                     return [ni,ni2 + 1]
# sys.exit(Solution.twoSum([1,2,3],5))
#     # def main:
#     #     print (twoSum([1,2,3],5))


from typing import List
import sys
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:       
        for i , n in enumerate(nums):
            elem = target - n
            x = nums.index(elem) if elem in nums else -1
            if x > -1:
                return [i,x]
        
sys.exit(Solution.twoSum([1,2,3],5))