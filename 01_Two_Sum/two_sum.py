from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers such that they add up to target, if given an array of
        integers nums and an integer target.

        Constraints:
        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.
        """
        if not 2 <= len(nums) <= 10**4:
            raise ValueError("The length of nums must be between 2 and 10^4.")

        if not all(-(10**9) <= num <= 10**9 for num in nums):
            raise ValueError("Each number in nums must be between -10^9 and 10^9.")

        if not -(10**9) <= target <= 10**9:
            raise ValueError("The target must be between -10^9 and 10^9.")

        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num  # complement of the current number
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        raise ValueError("No two sum solution found.")

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Solve with the brute-force approach to solving the Two Sum problem.
        This approach checks every possible pair of numbers in the list to see if they add up to the
        target. While this method is intuitive and straightforward, it is less efficient compared to
        using a hash table.
        Humanoid Thinking: Easy to think of and implement but inefficient.
        Time Complexity: ({O}(n^2)) due to the nested loops.
        Space Complexity: ({O}(1)) as no extra space is used apart from variables for indexing.
        """
        # Outer loop: iterate through each element by index 'i'
        for i, _ in enumerate(nums):
            # Inner loop: iterate through remaining elements by index 'j'
            for j in range(i + 1, len(nums)):
                # Check if the current pair adds up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ValueError("No two sum solution found.")
