#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:03:44 2020

@author: zhenyuxu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        slow = head.next
        fast = head.next.next
        while (fast and fast.next):
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
            