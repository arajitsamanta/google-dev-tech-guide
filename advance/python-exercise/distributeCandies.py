# distributeCandies.py

"""
https://leetcode.com/problems/distribute-candies/description/

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one 
candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of 
kinds of candies the sister could gain.

Example 1
=========
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

Example 2
=========
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.

Complexity Analysis
===================
Time complexity : O(n) The entire candiescandies array is traversed only once. Here, nn refers to the size of candiescandies array.

Space complexity : O(n). set will be of size nn in the worst case.
"""
class DistributeCandies:
    def perfomrDistribution(self, candies):
        """
        :type candies: List[int]
        :rtype: int

        The maximum no. of unique candies which the girl can obtain could be atmost n/2n/2, where nn refers to the number of candies. 
        Further, in case the number of unique candies are below n/2n/2, to maximize the number of unique candies that the girl will obtain, 
        we'll assign all the unique candies to the girl. Thus, in such a case, the number of unique candies the girl gets is equal to the 
        total number of unique candies in the given candiescandies array.
        """
        return min(len(set(candies)), len(candies)//2)
