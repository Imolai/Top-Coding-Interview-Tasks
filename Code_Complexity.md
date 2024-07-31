# Code Complexity

## Contents

- [Code Complexity](#code-complexity)
  - [Contents](#contents)
  - [What is Big O Complexity](#what-is-big-o-complexity)
    - [1. Identify the Basic Operations](#1-identify-the-basic-operations)
    - [2. Count the Number of Operations](#2-count-the-number-of-operations)
    - [3. Consider the Worst-Case Scenario](#3-consider-the-worst-case-scenario)
    - [4. Use Summations for Loops and Recursions](#4-use-summations-for-loops-and-recursions)
    - [5. Drop Constant Factors and Non-Dominant Terms](#5-drop-constant-factors-and-non-dominant-terms)
    - [6. Combine Complexities](#6-combine-complexities)
    - [Examples of Common Patterns:](#examples-of-common-patterns)
    - [Space Complexity](#space-complexity)
    - [Practical Tips:](#practical-tips)
    - [Common Big O Notations:](#common-big-o-notations)
  - [How Can We Decrease Complexity](#how-can-we-decrease-complexity)
    - [1. Identify Bottlenecks](#1-identify-bottlenecks)
    - [2. Optimize Loops and Recursions](#2-optimize-loops-and-recursions)
    - [3. Use Efficient Data Structures](#3-use-efficient-data-structures)
    - [4. Algorithm Design Techniques](#4-algorithm-design-techniques)
    - [5. Avoid Redundant Computations](#5-avoid-redundant-computations)
    - [6. Reduce Input Size](#6-reduce-input-size)
    - [7. Use Mathematical Insights](#7-use-mathematical-insights)
    - [Practical Tips and Examples](#practical-tips-and-examples)
    - [Summary](#summary)

## What is Big O Complexity

Estimating the **Big O** complexity of an algorithm involves analyzing its performance in terms of time (how long it takes to run) or space (how much memory it uses) as the input size grows. Here’s a step-by-step method to determine the Big O complexity:

### 1. Identify the Basic Operations
The first step is to identify the fundamental operations of the algorithm, such as comparisons, assignments, arithmetic operations, and so on. These are the operations that will contribute to the time or space complexity.

### 2. Count the Number of Operations
Next, count how many times each fundamental operation is executed relative to the input size \( n \). This involves looking at loops, recursive calls, and other constructs that repeat operations.

### 3. Consider the Worst-Case Scenario
Big O notation describes the worst-case scenario of an algorithm's growth rate. Therefore, you need to analyze the algorithm for the maximum possible number of operations it might perform.

### 4. Use Summations for Loops and Recursions
For iterative algorithms with loops, consider the number of iterations:
- **Single loop**: If a single loop runs \( n \) times, the complexity is \( O(n) \).
- **Nested loops**: If a loop runs inside another loop, each running \( n \) times, the complexity is \( O(n^2) \).

For recursive algorithms, use recurrence relations to express the complexity:
- For example, the recurrence relation for the Merge Sort algorithm is \( T(n) = 2T(n/2) + O(n) \). Solving this gives \( T(n) = O(n \log n) \).

### 5. Drop Constant Factors and Non-Dominant Terms
Big O notation focuses on the asymptotic behavior, so constant factors and less significant terms are ignored:
- For example, \( O(2n) \) simplifies to \( O(n) \) and \( O(n^2 + n) \) simplifies to \( O(n^2) \).

### 6. Combine Complexities
If an algorithm has multiple independent parts, their complexities are added:
- For instance, if one part of an algorithm runs in \( O(n) \) and another in \( O(n^2) \), the overall complexity is \( O(n^2) \).

### Examples of Common Patterns:
1. **Iterative Algorithms**:
    ```python
    def example(n):
        for i in range(n):
            # O(1) operation
    ```
    - Each iteration of the loop takes constant time \( O(1) \), and the loop runs \( n \) times. So, the overall complexity is \( O(n) \).

2. **Nested Loops**:
    ```python
    def example(n):
        for i in range(n):
            for j in range(n):
                # O(1) operation
    ```
    - The inner loop runs \( n \) times for each iteration of the outer loop, leading to \( O(n^2) \) complexity.

3. **Recursive Algorithms**:
    ```python
    def example(n):
        if n <= 1:
            return n
        else:
            return example(n-1) + example(n-1)
    ```
    - This is a classic example of a recursive function with exponential growth, leading to \( O(2^n) \).

### Space Complexity
Similarly, analyze how the memory usage grows:
- **Recursive calls**: Consider the stack space required for recursive calls.
- **Auxiliary data structures**: Consider the space used by additional data structures like arrays, hash maps, etc.

### Practical Tips:
- **Use the Master Theorem** for divide-and-conquer recurrences.
- **Analyze the control flow**: Look at if-else branches, loops, and recursive calls.
- **Compare with known patterns**: Many algorithms fall into known categories with established complexities (e.g., sorting algorithms, searching algorithms).

### Common Big O Notations:
- \( O(1) \): Constant time
- \( O(log n) \): Logarithmic time
- \( O(n) \): Linear time
- \( O(n log n) \): Linearithmic time
- \( O(n^2) \): Quadratic time
- \( O(2^n) \): Exponential time
- \( O(n!) \): Factorial time

By following these steps, you can systematically estimate the Big O complexity of a given algorithm. 

> For further detailed examples and exercises, resources like [GeeksforGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/) and the [CLRS textbook](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) are highly recommended.

## How Can We Decrease Complexity

To decrease the Big O complexity of an algorithm and eliminate the pain points, follow these practical tips and rules of thumb:

### 1. Identify Bottlenecks
- **Profile the Code**: Use profiling tools to identify the parts of your code that take the most time. This can highlight inefficient loops or recursive calls.
- **Complexity Analysis**: Break down the algorithm into individual components and analyze their complexities. Identify the parts that have the highest growth rate.

### 2. Optimize Loops and Recursions
- **Reduce Nested Loops**: Minimize the depth of nested loops. If you have a double loop (`O(n^2)`), look for ways to reduce it to a single loop (`O(n)`).
    - **Example**: Replace nested loops that check all pairs with more efficient data structures (e.g., using a hash set for membership tests).
- **Memoization and Dynamic Programming**: Use memoization to store results of expensive function calls and avoid redundant calculations. Convert recursive algorithms to dynamic programming where possible.
    - **Example**: Fibonacci sequence using memoization reduces from `O(2^n)` to `O(n)`.

### 3. Use Efficient Data Structures
- **Hash Tables and Sets**: Use hash tables (dictionaries) and sets for faster lookups instead of lists. This can reduce `O(n)` lookups to `O(1)`.
    - **Example**: Using a set to check for duplicates instead of nested loops.
- **Heaps**: For problems involving finding the minimum or maximum elements repeatedly, use heaps.
    - **Example**: Finding the k-th largest element can be optimized using a min-heap to `O(n log k)` instead of sorting the entire list (`O(n log n)`).

### 4. Algorithm Design Techniques
- **Divide and Conquer**: Break the problem into smaller sub-problems, solve them independently, and combine the results.
    - **Example**: Merge Sort and Quick Sort use divide and conquer to achieve `O(n log n)` complexity.
- **Greedy Algorithms**: Make a series of choices that seem optimal at each step. This can sometimes provide efficient solutions.
    - **Example**: The activity selection problem can be solved in `O(n log n)` using a greedy approach.

### 5. Avoid Redundant Computations
- **Precompute Results**: If the same computations are repeated, consider precomputing and storing the results.
    - **Example**: Precompute prefix sums for range sum queries to reduce from `O(n)` to `O(1)` for each query.
- **Cache Intermediate Results**: Store intermediate results in a cache to avoid recomputation.

### 6. Reduce Input Size
- **Filtering and Pruning**: Reduce the size of the input by filtering out unnecessary elements or pruning the search space.
    - **Example**: In backtracking problems, prune branches that cannot possibly lead to a solution.

### 7. Use Mathematical Insights
- **Mathematical Formulas**: Replace iterative calculations with direct mathematical formulas when possible.
    - **Example**: Sum of the first n natural numbers can be computed in `O(1)` using the formula \( n(n + 1)/2 \).

### Practical Tips and Examples

1. **From O(n^2) to O(n)**:
    ```python
    # Original O(n^2) approach
    def check_duplicates(arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False

    # Optimized O(n) approach using a set
    def check_duplicates(arr):
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False
    ```

2. **From Exponential to Linear with Memoization**:
    ```python
    # Original O(2^n) Fibonacci
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)

    # Optimized O(n) Fibonacci with memoization
    def fib(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
    ```

3. **Using Binary Search to Reduce Complexity**:
    ```python
    # Original O(n) search
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    # Optimized O(log n) search using binary search (requires sorted array)
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    ```

### Summary

To reduce the Big O complexity of an algorithm:

1. Identify and eliminate bottlenecks.
2. Optimize loops and recursion.
3. Use efficient data structures.
4. Apply algorithm design techniques like divide and conquer, and greedy algorithms.
5. Avoid redundant computations by caching or precomputing results.
6. Reduce input size through filtering and pruning.
7. Use mathematical insights to simplify computations.

By systematically applying these strategies, we can transform inefficient algorithms into efficient ones.
