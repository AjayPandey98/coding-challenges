# https://leetcode.com/problems/validate-binary-search-tree/

import timeit
from typing import Optional

from data import TreeNode, deserializeStringArrayToBinaryTree

# Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

# Use a sub-function to explore each branch of the current tree recursively in pre-order.
# Pass the sub-function a min and max value that represent the currently acceptable boundaries.
# Check that the root node value is within boundaries and use the root node value to update the
# call for the left, and right, branches of the sub-tree.
#
# Time complexity - O(n)
# The algorithm will visit each tree node of a valid tree, it will fail faster for invalid trees.
# Space complexity - O(n)
# The size of the call stack will grow in size linearly with the size of the input
#
# Runtime: 66 ms, faster than 55.73% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.6 MB, less than 44.99% of Python3 online submissions for Validate Binary Search Tree.
class DFSWithBounds:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Description guarantees that we will have a minimum of 1 node
        # if not root:
        #     return True

        # A valid BST is defined as follows:
        # The left subtree of a node contains only nodes with keys less than the node's key.
        # The right subtree of a node contains only nodes with keys greater than the node's key.
        # Both the left and right subtrees must also be binary search trees.

        def isValidBoundedBST(root: TreeNode, min: int, max: int) -> bool:
            # It is easier to read checking the root on the return statement, but quicker to
            # check if the root is valid before we explore the sub-trees.
            if not (min < root.val < max):
                return False
            # If we have a left branch, DFS check whether the whole branch is between min and root
            if root.left and not isValidBoundedBST(root.left, min, root.val):
                return False
            if root.right and not isValidBoundedBST(root.right, root.val, max):
                return False

            # If root, right and left sub-trees are valid
            return True

        # Initial call
        return isValidBoundedBST(root, float("-inf"), float("inf"))


# DFS in-order transversal without recursion
#
# Time complexity - O(n)
# The algorithm will visit each tree node of a valid tree, it will fail faster for invalid trees.
# Space complexity - O(n)
# The size of the stack will grow in size linearly with the size of the input up to a max of n/2
#
# Runtime: 66 ms, faster than 55.73% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 78.56% of Python3 online submissions for Validate Binary Search Tree.
class InOrderTransversal:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current = root
        stack = []
        last = float("-inf")
        while True:

            # While the current node has a left value, push it into the stack
            if current:
                stack.append(current)
                current = current.left

            # When we run out of left nodes, pop the next "root" node from the stack
            elif stack:
                current = stack.pop()
                # Nodes visited should have strictly increasing values
                if current.val <= last:
                    return False

                # Update the last visited node value and the current pointer
                last = current.val
                current = current.right

            # Once we explore all nodes, if all values found on the in-order traversal were in strictly
            # increasing order, the BST is valid.
            else:
                return True


def test():
    executors = [InOrderTransversal, DFSWithBounds]
    tests = [
        ["[1,1]", False],
        ["[2,1,3]", True],
        ["[5,1,4,null,null,3,6]", False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1e4"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.isValidBST(deserializeStringArrayToBinaryTree(t[0]))
                expected = t[1]
                assert (
                    result == expected
                ), f"\033[93m» {result} <> {expected}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
