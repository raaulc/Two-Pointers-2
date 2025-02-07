from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # No need to modify if size is already ≤ 2

        insert_pos = 2  # Allow first two elements by default

        for i in range(2, len(nums)):
            if nums[i] != nums[insert_pos - 2]:  # Ensure at most 2 occurrences
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos  # New length of modified nums
