// ALL TESTS PASSED
// Time Complexity: O(n)
// Runtime: 2ms (beats 89.92%)
// Memory: 129.28MB (beats 80.00%)
// 
// Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
// If no such indices exists, return false.
//
// Example 1:
//      Input: nums = [1,2,3,4,5]
//      Output: true
//      Explanation: Any triplet where i < j < k is valid.
// Example 2:
//      Input: nums = [5,4,3,2,1]
//      Output: false
//      Explanation: No triplet exists.
// Example 3:
//      Input: nums = [2,1,5,0,4,6]
//      Output: true
//      Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (int num : nums) {
            first = (num <= first) ? num : first;
            second = (num > first && num <= second) ? num : second;

            if (num > second) {
                return true;
            }
        }

        return false;
    }
}