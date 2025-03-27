# Random Sort

A Python library that implements an "innovative" sorting algorithm based on randomization.

## Installation

```bash
pip install random_sort
```

## Usage

```python
from random_sort import random_sort

# Create an unsorted list
my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort the list with random_sort
sorted_list = random_sort(my_list)

print(sorted_list)  # [1, 1, 2, 3, 4, 5, 6, 9]

# You can also specify a maximum number of attempts
sorted_list = random_sort(my_list, max_attempts=50)
```

## How it works

The `random_sort` algorithm uses a revolutionary approach to sorting:

1. Completely randomize the list
2. Check if it happens to be sorted
3. If not sorted, repeat from step 1 until you get a sorted list
4. If it takes too many attempts, it falls back to the built-in sorting algorithm

This algorithm has a time complexity of O(∞) in the worst case theoretically, but in practice it's limited by the max_attempts parameter to avoid infinite recursion.

## Warning

This library was created for humorous purposes. Don't use it in production environments, unless you have infinite time at your disposal and would like to use it creatively.

## License

MIT 