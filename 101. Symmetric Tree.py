#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:08:28 2020

@author: zhenyuxu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSym(root.left, root.right)
        
    def isSym(self, node_one, node_two):
        if node_one is None and node_two is None:
            return True
        elif node_one is None or node_two is None:
            return False
        elif node_one.val != node_two.val:
            return False
        return self.isSym(node_one.left, node_two.right) and self.isSym(node_one.right, node_two.left)
    