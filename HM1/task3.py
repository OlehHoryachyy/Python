#====Task 3====

"""You are given an array of integers. You should find the sum of the elements with even indexes
(0th, 2nd, 4th...) then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer.
Example:
your_function([0, 1, 2, 3, 4, 5]) == 30
your_function([1, 3, 5]) == 30
your_function([6]) == 36
your_function([]) == 0"""

def your_function(list):
    if len(list) == 0:
        return 0
    res = sum(list[::2])
    res *= list[len(list) - 1]
    return res

print your_function([0])