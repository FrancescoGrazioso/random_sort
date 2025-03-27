# Random Sort

A Python library that implements an "innovative" sorting algorithm based on randomization.

[![GitHub License](https://img.shields.io/github/license/FrancescoGrazioso/random_sort)](https://github.com/FrancescoGrazioso/random_sort/blob/main/LICENSE)
[![PyPI Version](https://img.shields.io/badge/pypi-v0.1.1-blue)](https://github.com/FrancescoGrazioso/random_sort/releases)

## Description

Random Sort implements the classic "Bogosort" algorithm as a joke/educational library. It repeatedly shuffles a list randomly until it happens to be sorted. This is of course extremely inefficient (with an average case of O(n × n!)) and is intended for fun and education about algorithm efficiency, not for actual use.

## Installation

```bash
# From PyPI (when published)
pip install random_sort

# Directly from GitHub
pip install git+https://github.com/FrancescoGrazioso/random_sort.git
```

## Usage

```python
from random_sort import random_sort, bogosort

# Create an unsorted list
my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort the list with random_sort
sorted_list = random_sort(my_list)

print(sorted_list)  # [1, 1, 2, 3, 4, 5, 6, 9]

# You can also use the alias 'bogosort'
sorted_list = bogosort(my_list)

# Control the maximum number of attempts
sorted_list = random_sort(my_list, max_attempts=50)

# Get verbose output
sorted_list = random_sort(my_list, verbose=True)

# Sort using a key function (like the built-in sort)
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people = random_sort(people, key=lambda x: x["age"])
```

## How it works

The `random_sort` algorithm uses a revolutionary approach to sorting:

1. Completely randomize the list
2. Check if it happens to be sorted
3. If not sorted, repeat from step 1 until you get a sorted list
4. If it takes too many attempts, it falls back to the built-in sorting algorithm

This algorithm has a time complexity of O(∞) in the worst case theoretically, but in practice it's limited by the max_attempts parameter to avoid infinite recursion.

## Features

- Implements the classic "Bogosort" algorithm
- Prevents infinite recursion with configurable max attempts
- Provides verbose mode to see the sorting progress
- Supports key functions just like Python's built-in sort
- Early termination for lists that are too large
- 100% test coverage

## Performance

Below is a table showing the expected number of attempts needed to sort lists of different sizes:

| List Size | Expected Attempts |
|-----------|------------------|
| 1         | 1                |
| 2         | 2                |
| 3         | 6                |
| 4         | 24               |
| 5         | 120              |
| 6         | 720              |
| 7         | 5,040            |
| 8         | 40,320           |
| 9         | 362,880          |
| 10        | 3,628,800        |

As you can see, the number of attempts grows factorially with the list size!

## Warning

This library was created for humorous and educational purposes. Don't use it in production environments, unless you have infinite time at your disposal and would like to use it creatively.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT 