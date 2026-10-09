# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    """Optimized solution using a dictionary to count occurrences."""
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n) for this implementation, because every element must
  be counted and the maximum frequency must be found.
- Worst-case: O(n), because the dictionary counts n elements and then
  examines at most n distinct keys to find the maximum.
- Average-case: O(n), assuming average O(1) dictionary operations.
- Space complexity: O(k), where k is the number of distinct values;
  worst-case O(n).
- Why this approach? A dictionary stores each value and its frequency,
  avoiding repeatedly scanning the entire list for every element.
- Could it be optimized? The original nested-loop approach below takes
  O(n^2) time. Replacing it with this dictionary-based solution reduces
  average time to O(n).
- Trade-offs: The dictionary uses extra memory, but saves time.
  Ties may return any of the most frequent values, as permitted.
"""


# Original version for comparison with the optimized solution.
def most_frequent_original(numbers):
    """Simple nested-loop approach, retained for comparison."""
    if not numbers:
        return None

    best_number = numbers[0]
    best_count = 0

    for number in numbers:
        count = 0
        for candidate in numbers:
            if candidate == number:
                count += 1

        if count > best_count:
            best_number = number
            best_count = count

    return best_number


# Optimization comparison:
# Original: O(n^2) time, O(1) auxiliary space.
# Optimized: O(n) average time, O(k) auxiliary space.
# The dictionary trades additional memory for much faster counting.


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    """Remove duplicates using a set while preserving first occurrence."""
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), even if all values are equal, because every element
  must be examined.
- Worst-case: O(n) average-case dictionary/set operations; pathological
  hash collisions can increase the cost.
- Average-case: O(n), with average O(1) set membership and insertion.
- Space complexity: O(n) for the set and output list in the worst case.
- Why this approach? A set tracks values already encountered while a
  separate list preserves their original order.
- Could it be optimized? The same general approach is efficient.
  Returning a generator could reduce output memory if a list were not
  required, but this prompt requires a list.
- Trade-offs: Extra memory is used to avoid slower repeated list searches.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list
# that sum to a target. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    """Find pairs using previously seen numbers."""
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n), since every number is examined, even when no pairs exist.
- Worst-case: O(n^2) if hash operations suffer pathological collisions;
  under normal hash-set behavior, the algorithm takes O(n + p), where
  p is the number of returned pairs.
- Average-case: O(n + p), or O(n^2) when the output itself contains
  O(n^2) pairs in the general case. This prompt assumes no duplicate
  input values, so at most floor(n/2) disjoint complement matches occur.
- Space complexity: O(n + p) for the set and output pairs.
- Why this approach? Each number is checked against the set of earlier
  numbers, so each valid pair is discovered once.
- Could it be optimized? This is already efficient for unsorted input.
  Sorting and using two pointers is another O(n log n) approach.
- Trade-offs: The set uses extra memory but avoids nested-loop searching.
  Output order is not guaranteed or required.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Add n elements to a simulated dynamic array with a fixed initial capacity.
# When full, double the capacity and copy existing values.

def add_n_items(n):
    """Simulate appending n items to a dynamic array."""
    if n < 0:
        raise ValueError("n must be non-negative")

    capacity = 2
    storage = [None] * capacity
    size = 0

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_storage = [None] * new_capacity

            for index in range(size):
                new_storage[index] = storage[index]

            print(
                f"Resizing: capacity {capacity} -> {new_capacity}; "
                f"copied {size} items"
            )

            storage = new_storage
            capacity = new_capacity

        storage[size] = number
        size += 1

    return storage[:size]


"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the array is full, before the next append.
  Starting at capacity 2, capacities double to 4, 8, 16, and so on.
- What is the worst-case for a single append? O(n) when a resize copies
  all n existing elements.
- What is the amortized time per append overall? O(1). Across n appends,
  the total number of copied elements is bounded by a geometric series,
  so total work is O(n).
- Space complexity: O(n) for the dynamic array. During resizing, old and
  new arrays coexist temporarily, but peak memory is still O(n).
- Why does doubling reduce the cost overall? Resizing occurs less often
  as the array grows. The cost of occasional large copies is spread over
  many inexpensive appends.
- Trade-offs: Doubling uses spare capacity and temporary memory during
  resizing, but avoids copying on every append. This function simulates
  the behavior; it does not expose Python's actual list capacity.
"""


# 🔍 Problem 5: Compute Running Totals
# Return a new list where each element is the sum of all elements up to
# that index.

def running_total(nums):
    """Compute cumulative sums in one pass."""
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because each input number must be processed.
- Worst-case: O(n), because the function performs one pass over the list.
- Average-case: O(n), for the same reason.
- Space complexity: O(n) for the output list; O(1) auxiliary space
  beyond that output.
- Why this approach? Keeping a running sum avoids recalculating the sum
  of all earlier elements at every position.
- Could it be optimized? Not asymptotically when a new output list is
  required; every element must be processed and returned.
- Trade-offs: The output requires O(n) memory, but the algorithm is
  straightforward and avoids repeated summation.


# TEST CASES
# Run this file directly to execute all tests.
"""

import unittest


class PerformanceLabTests(unittest.TestCase):

    # Problem 1 tests
    def test_most_frequent_example(self):
        self.assertEqual(most_frequent([1, 3, 2, 3, 4, 1, 3]), 3)

    def test_most_frequent_single_value(self):
        self.assertEqual(most_frequent([7]), 7)

    def test_most_frequent_empty(self):
        self.assertIsNone(most_frequent([]))

    def test_most_frequent_all_equal(self):
        self.assertEqual(most_frequent([5, 5, 5]), 5)

    def test_most_frequent_tie(self):
        result = most_frequent([1, 1, 2, 2])
        self.assertIn(result, [1, 2])

    def test_optimized_matches_original(self):
        numbers = [4, 2, 4, 3, 2, 4, 5]
        self.assertEqual(
            most_frequent(numbers),
            most_frequent_original(numbers)
        )

    # Problem 2 tests
    def test_remove_duplicates_example(self):
        self.assertEqual(
            remove_duplicates([4, 5, 4, 6, 5, 7]),
            [4, 5, 6, 7]
        )

    def test_remove_duplicates_empty(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_all_equal(self):
        self.assertEqual(remove_duplicates([2, 2, 2]), [2])

    def test_remove_duplicates_preserves_order(self):
        self.assertEqual(
            remove_duplicates([3, 1, 3, 2, 1]),
            [3, 1, 2]
        )

    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    # Problem 3 tests
    def test_find_pairs_example(self):
        self.assertEqual(
            set(find_pairs([1, 2, 3, 4], 5)),
            {(1, 4), (2, 3)}
        )

    def test_find_pairs_no_matches(self):
        self.assertEqual(find_pairs([1, 2, 3], 20), [])

    def test_find_pairs_empty(self):
        self.assertEqual(find_pairs([], 5), [])

    def test_find_pairs_negative_numbers(self):
        self.assertEqual(
            set(find_pairs([-3, -1, 1, 3], 0)),
            {(-3, 3), (-1, 1)}
        )

    def test_find_pairs_one_match(self):
        self.assertEqual(find_pairs([2, 8], 10), [(2, 8)])

    # Problem 4 tests
    def test_add_n_items_empty(self):
        self.assertEqual(add_n_items(0), [])

    def test_add_n_items_within_capacity(self):
        self.assertEqual(add_n_items(2), [0, 1])

    def test_add_n_items_triggers_resize(self):
        self.assertEqual(add_n_items(3), [0, 1, 2])

    def test_add_n_items_multiple_resizes(self):
        self.assertEqual(add_n_items(9), list(range(9)))

    def test_add_n_items_negative(self):
        with self.assertRaises(ValueError):
            add_n_items(-1)

    # Problem 5 tests
    def test_running_total_example(self):
        self.assertEqual(running_total([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_running_total_empty(self):
        self.assertEqual(running_total([]), [])

    def test_running_total_negative_numbers(self):
        self.assertEqual(running_total([5, -2, 3]), [5, 3, 6])

    def test_running_total_single_value(self):
        self.assertEqual(running_total([8]), [8])

    def test_running_total_zeroes(self):
        self.assertEqual(running_total([0, 0, 0]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)