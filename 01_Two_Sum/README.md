# Two Sum Task

## Contents

- [Two Sum Task](#two-sum-task)
  - [Contents](#contents)
  - [First Approach](#first-approach)
    - [Brute-Force (Nested Loop) Approach](#brute-force-nested-loop-approach)
    - [Implementation:](#implementation)
    - [Step-by-Step Execution:](#step-by-step-execution)
    - [Example Execution:](#example-execution)
    - [Summary:](#summary)
  - [The Refined Approach](#the-refined-approach)
    - [Starting Point: Brute-Force Method](#starting-point-brute-force-method)
    - [Optimization Thought Process](#optimization-thought-process)
      - [Step-by-Step Optimization](#step-by-step-optimization)
    - [Transition from Brute-Force to Optimized with Complements:](#transition-from-brute-force-to-optimized-with-complements)
    - [Full Optimized Implementation:](#full-optimized-implementation)
    - [Detailed Step-by-Step Explanation:](#detailed-step-by-step-explanation)
    - [Conclusion](#conclusion)

## First Approach

The first humanoid thinking would be looping over the nums and at every number value, starting an additional loop till the end of the nums and checking is the target reached or not.
This is the brute-force approach to solving the Two Sum problem. This approach checks every possible pair of numbers in the list to see if they add up to the target. While this method is intuitive and straightforward, it is less efficient compared to using a hash table.

### Brute-Force (Nested Loop) Approach

**Algorithm Explanation:**

1. **Initialize Outer Loop**: Iterate through the list `nums`, considering each element as the first number.
2. **Initialize Inner Loop**: For each element in the outer loop, iterate through the remaining elements as potential second numbers.
3. **Check Sum**: For each pair, check if their sum equals the target.
4. **Return Indices**: If a pair is found that sums to the target, return their indices.

### Implementation:

Here is the brute-force solution implemented in Python:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Outer loop: iterate through each element by index 'i'
        for i in range(len(nums)):
            # Inner loop: iterate through remaining elements by index 'j'
            for j in range(i + 1, len(nums)):
                # Check if the current pair adds up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ValueError("No two sum solution found.")
```

### Step-by-Step Execution:

1. **Outer Loop Initialization**:
    - Start with the first element, then move to the second, third, etc.
    ```python
    for i, _ in enumerate(nums):
    ```

2. **Inner Loop Initialization**:
    - For the current element in the outer loop (`nums[i]`), iterate through the subsequent elements in the list (`nums[j]`).
    ```python
    for j in range(i + 1, len(nums)):
    ```

3. **Check Sum**:
    - Check if the sum of the elements at indices `i` and `j` equals the target.
    ```python
    if nums[i] + nums[j] == target:
    ```

4. **Return Indices**:
    - As soon as a valid pair is found, return the indices `[i, j]`.
    ```python
    return [i, j]
    ```

### Example Execution:

For `nums = [2, 7, 11, 15]` and `target = 9`:
- Outer loop starts with `i = 0` (`nums[i] = 2`).
- Inner loop starts with `j = 1` (`nums[j] = 7`).
- Check if `nums[0] + nums[1] == 9`.
- It matches the target, so return `[0, 1]`.

### Summary:

- **Humanoid Thinking**: Easy to think of and implement but inefficient.
- **Time Complexity**: {O}(n^2) due to the nested loops.
- **Space Complexity**: {O}(1) as no extra space is used apart from variables for indexing.

The brute-force (nested loop) approach is the first natural way to think about finding pairs, especially when formalizing the problem-solving process without considering optimization initially.

## The Refined Approach

Let's trace the thought process from the brute-force method to the optimized solution using the idea of complements.

### Starting Point: Brute-Force Method

**Brute-Force Method:**

1. **Initialize Outer Loop**: Iterate through each element in the list.
2. **Initialize Inner Loop**: For each element in the outer loop, iterate through the remaining elements.
3. **Check Sum**: For each pair, check if their sum equals the target.
4. **Return Indices**: If a pair is found, return their indices.

This method checks every possible pair, resulting in a time complexity of {O}(n^2).

### Optimization Thought Process

To optimize, we need to reduce the number of comparisons from the nested loop structure to a more efficient way. The key idea here is to use a hash table (dictionary in Python) to store and quickly lookup indices.

#### Step-by-Step Optimization

1. **Recognize the Redundancy**: In the brute-force method, we are repeatedly checking pairs, many of which are unnecessary once we've seen certain elements. Can we avoid re-checking these pairs?
2. **Use a Hash Table**: We can use a hash table to store elements we've seen so far, allowing for O(1) average-time complexity lookups.
3. **Identify the Complement**: For each element `num` at index `i`, the complement needed to reach the target is `complement = target - num`. If we can check if this complement has been seen before, we can immediately identify the pair.

### Transition from Brute-Force to Optimized with Complements:

**Step 1: Hash Table for Storage**:

- Store each element's value and its index in a hash table as we iterate through the list.

**Step 2: Complement Calculation**:

- For each element, calculate the required complement to hit the target sum.

**Step 3: Check for Complement in Hash Table**:

- Check if the complement exists in the previously stored elements (hash table).

**Step 4: Return Indices**:

- If the complement exists, return the indices of the current element and the complement.

**Key Optimization Insight**:

- By instantly checking for the complement, we avoid the second loop and reduce the complexity from {O}(n^2) to {O}(n).

### Full Optimized Implementation:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        raise ValueError("No two sum solution found.")
```

### Detailed Step-by-Step Explanation:

1. **Initialize an Empty Dictionary**:
    - `num_dict = {}`

2. **Iterate Through the List**:
    ```python
    for i, num in enumerate(nums):
    ```

3. **Calculate the Complement**:
    ```python
    complement = target - num
    ```
    - For `num`, compute the `complement` needed to reach `target`.

4. **Check if Complement Exists in Dictionary**:
    ```python
    if complement in num_dict:
    ```
    - Look into the dictionary to see if this complement has been seen (stored).

5. **Return Indices if Complement is Found**:
    ```python
    return [num_dict[complement], i]
    ```
    - If the complement exists, obtain its stored index (`num_dict[complement]`) and current index (`i`).

6. **Store Current Element and Index in Dictionary**:
    ```python
    num_dict[num] = i
    ```
    - Add the current element and its index to the dictionary for future reference.

### Conclusion

**Thinking Process**:

- **Brute-Force Awareness**: Recognize that checking all pairs is inefficient.
- **Introduce Hash Table**: Use it to store and lookup indices efficiently.
- **Complement Concept**: Compute the required complement for each element and check if it's already been seen.
- **Immediate Returns**: Leverage the hash table lookups to directly return results without another loop.

This journey from brute-force to an efficient solution showcases how recognizing redundancies and using appropriate data structures (hash tables) can lead to significant optimizations.
