#!/usr/bin/env python

def get_one_peer(nums, target):
    to_map = {}
    length = len(nums)
    for i in range(length):
        to_map[nums[i]] = i
        for_peer = target - nums[i]
        if for_peer in to_map:
            return to_map[for_peer],i
    else:
        return None

nums = [1,2,3,4,5,6]
print(get_one_peer(nums,11)) 
