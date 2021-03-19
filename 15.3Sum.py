"""
URL: https://leetcode.com/problems/3sum/
https://afteracademy.com/problems/triplet-with-zero-sum
Description: 
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triplets.add(f'{nums[i]}, {nums[left]}, {nums[right]}')
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return [map(int, triplet.split(',')) for triplet in triplets]
