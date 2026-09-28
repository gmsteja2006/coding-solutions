# Sliding Window Maximum

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return  *the max sliding window*.

 

 **Example 1:** 

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```

 **Example 2:** 

```
Input: nums = [1], k = 1
Output: [1]

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- 1 <= k <= nums.length

## Solution

**Language:** Python  
**Runtime:** 266 ms (beats 78.01%)  
**Memory:** 28.6 MB (beats 72.46%)  
**Submitted:** 2026-09-28T10:23:15.327Z  

```py
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()   
        result = []

        for i in range(len(nums)):
           
            if dq and dq[0] == i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            
            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

```

---

[View on LeetCode](https://leetcode.com/problems/sliding-window-maximum/)