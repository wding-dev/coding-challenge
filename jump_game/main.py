"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
"""

from typing import List


def solution(nums: List[int]) -> bool:
    """
    Look at the list from backwards. 
    Eg: input=[3,2,1,0,4] -> [4,0,1,2,3].
    
    Following the new list, 
    if we can find an element whose value is greater than its gap between index of this element and index of the target, 
    then this element will be a new target for the following elements to reach.
    
    Repeating this logic, as long as the last element of the reversed list (the first element based on the input)
    can reach the last target, it will be able to reach the end.
    """
    nums.reverse()

    result = False
    target_idx = 0

    for idx, num in enumerate(nums):
        if num < (idx - target_idx):
            result = False
        else:
            result = True
            target_idx = idx

    return result
