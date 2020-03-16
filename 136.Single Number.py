#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:01:54 2020

@author: zhenyuxu
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =  nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result