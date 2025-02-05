# Problem: Contains Duplicate

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example:

```plaintext
Input: nums = [1,2,3,1]
Output: true
```

```plaintext
Input: nums = [1,2,3,4]
Output: false
```

## Approach

The first approach uses a set to track the elements we encounter as we iterate through the array. A set is a collection of unique items, meaning it automatically handles duplicates for us. Here's the breakdown of the approach:

1. **Initialize a Set**: We begin by initializing an empty set called `numSet`.
2. **Iterate through the List**: We then iterate through each element in the input list `nums`.
3. **Check for Duplicates**: For each element `n`, we check if it is already in the set `numSet`.
   - If it is, that means we have encountered a duplicate, and we return `True` immediately.
   - If it’s not in the set, we add it to the set and continue.
4. **Return False**: If no duplicates are found after checking all the elements, we return `False`.

This is a greedy approach where we use the set to optimize the search for previously encountered elements.

## Python Code Implementation

```python
class Solution:
    def containsDuplicateWithSet(self, nums: List[int]) -> bool:
        # Initialize an empty set to track encountered numbers
        numSet = set()

        # Iterate through the input list
        for n in nums:
            # If the number is already in the set, a duplicate is found
            if n in numSet:
                return True
            else:
                # Add the number to the set if it's not already present
                numSet.add(n)

        # If no duplicates are found, return False
        return False
```

## Explanation:

- **Set Operations**: The set `numSet` is used to store the unique elements we have seen so far. We take advantage of the set’s average O(1) time complexity for both `add()` and `in` operations. This is crucial for making the solution efficient.

## Time Complexity:

- **Time Complexity**: O(n), where `n` is the number of elements in the input list `nums`.

  - We are iterating through the entire list once, and each operation (checking for existence and adding an element to the set) takes constant time on average.

- **Space Complexity**: O(n), where `n` is the number of unique elements in the list.
  - In the worst case, all the elements in `nums` are unique, so we end up storing all `n` elements in the set.

## Edge Cases:

- **An empty list `[]`**: The function will return `False` because there are no elements to check for duplicates.
- **A list with one element `[1]`**: The function will return `False` because a single element cannot have a duplicate.

## Conclusion

This is an efficient solution for the "Contains Duplicate" problem, with optimal time complexity of O(n) and space complexity of O(n). Using a set ensures that we can check for duplicates in constant time on average.

This approach is one of the most straightforward and widely used methods for solving the problem, and it's a great starting point for understanding how to leverage sets in Python for duplicate detection.
