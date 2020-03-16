#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:53:02 2020

@author: zhenyuxu
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('Inf')
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            max_profit = max(max_profit, i - min_price)
        return max_profit