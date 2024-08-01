import unittest

from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example1(self):
        """
        Test Example 1.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self) -> None:
        """
        Test Example 2.

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        """
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self) -> None:
        """
        Test Example 3.

        Input: nums = [3,3], target = 6
        Output: [0,1]
        """
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_numbers_length(self) -> None:
        """
        Test Constraint 1.

        2 <= nums.length <= 10^4
        """
        with self.assertRaises(ValueError):
            self.solution.twoSum(list(range(1)), 0)
        with self.assertRaises(ValueError):
            self.solution.twoSum(list(range(10**4 + 1)), 0)

    def test_numbers_range(self) -> None:
        """
        Test Constraint 2.

        -10^9 <= nums[i] <= 10^9
        """
        with self.assertRaises(ValueError):
            self.solution.twoSum([-(10**9) - 1, 0], 0)
        with self.assertRaises(ValueError):
            self.solution.twoSum([10**9 + 1, 0], 0)

    def test_target_range(self) -> None:
        """
        Test Constraint 3.

        -10^9 <= target <= 10^9
        """
        with self.assertRaises(ValueError):
            self.solution.twoSum([-(10**9), -1], -(10**9) - 1)
        with self.assertRaises(ValueError):
            self.solution.twoSum([10**9, 1], 10**9 + 1)

    def test_no_solution(self) -> None:
        """
        Test no solution case (considered an edge case beyond typical constraints).
        """
        with self.assertRaises(ValueError):
            self.solution.twoSum([1, 2, 3], 10)
