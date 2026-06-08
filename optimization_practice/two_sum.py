"""
## 1. Two Sum (Find Two Numbers that Add to Target)  *(Easy)*

=================================================
TWO SUM
=================================================

Problem Statement:
Ydef two_sum_brute(nums, target):
    # Try every pair (i, j)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)


def two_sum_fast(nums, target):
    index_map = {}  # value -> index

    for i in range(len(nums)):
        x = nums[i]
        complement = target - x

        if complement in index_map:
            return (index_map[complement], i)

        index_map[x] = i


# Example input
nums = [2, 7, 11, 15]
target = 9

# Call both functions
print("Brute Force:", two_sum_brute(nums, target))
print("Optimized:", two_sum_fast(nums, target))

print("Brute Force Time Complexity: O(n^2)")
print("Optimized Time Complexity: O(n)")
-------------------------------------------------
Explanation:
For [2, 7, 11, 15] and target = 9:
   2 + 7 = 9
   indices -> (0, 1)

Brute force tries every pair, taking O(n^2)
time. The optimized version scans the list
ONCE and uses a dictionary to remember every
value it has already seen. As soon as the
complement (target - current) is found in
the dictionary, the answer is returned in
O(1) time, giving an overall O(n) algorithm.
=================================================

"""
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)


def two_sum_fast(nums, target):
    index_map = {}  

    for i in range(len(nums)):
        x = nums[i]
        complement = target - x

        if complement in index_map:
            return (index_map[complement], i)

        index_map[x] = i


nums = [2, 7, 11, 15]
target = 9

print("Brute Force:", two_sum_brute(nums, target))
print("Optimized:", two_sum_fast(nums, target))

print("Brute Force Time Complexity: O(n^2)")
print("Optimized Time Complexity: O(n)")