"""
Partitioning problem:

An arbitrary list of positive integers of any length and in any order
Determine if the list is partitionable or not. A partitioned list is one where it can be split into 2 sub-lists with equal sum. A sub-list can be any arbitrary (any set of numbers in any order) selection of numbers out of the parent list.

Enumerate the list of cases to solve to minimize execution time and provide the Order of the algorithm
Provide code showing the implementation in Python.

Example:

List = 1,2,3,4,5,6,7 = Partitionable 
List = 1,10,5,21,4 = Not Partitionable
List = 1,10,5,21,4,1 = Partitionable
"""

import unittest

def is_partitionable(arr):
    """
    an array will be partitionable only when array sum is even
    problem statement becomes find 2 subsets whose sum is equal
    the sum will be half of total sum of array
    """
    n = len(arr)
    arr_sum = sum(arr)
    # check if array sum is odd then array is not partitionable
    if arr_sum&1==1:
        return False
    required_sum = arr_sum//2

    dp = [[False for j in range(required_sum+1)] for i in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        dp[i][0] = True

    for i in range(n+1):
        for j in range(required_sum + 1):
            dp[i][j] = (dp[i-1][j]) or (dp[i-1][j-arr[i]])
    
    return dp[n][required_sum]


class TestPartition(unittest.TestCase):
    def test_is_partionable(self):
        self.assertEqual(is_partitionable([1,2,3,4,5,6,7]), True)
        self.assertEqual(is_partitionable([1,10,5,21,4]), False)
        self.assertEqual(is_partitionable([1,10,5,21,4, 1]), True)


if __name__=="__main__":
    unittest.main()