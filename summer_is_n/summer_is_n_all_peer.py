#!/usr/bin/env python

def get_all_peer(nums, target):
    to_map = {}
    res = []
    length = len(nums)
    for i in range(length):
        for_peer = target - nums[i]
        if for_peer in to_map:
            res.append((to_map[for_peer],i))
        to_map[nums[i]] = i
    return res

nums = [1,2,3,4,5,6]
print(get_all_peer(nums,9)) 
