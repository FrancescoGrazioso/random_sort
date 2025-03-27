import random
import sys
from typing import List, TypeVar

T = TypeVar('T')

def random_sort(arr: List[T], max_attempts: int = None) -> List[T]:
    """
    Sorts a list by randomly shuffling it until it happens to be sorted.
    
    Args:
        arr: The list to sort
        max_attempts: Maximum number of attempts before giving up and using 
                     a deterministic sort (default: uses sys.getrecursionlimit())
        
    Returns:
        The sorted list
    """
    # Set default max_attempts if not provided
    if max_attempts is None:
        # Use a sensible default to avoid recursion errors
        max_attempts = min(sys.getrecursionlimit() // 10, 100)
        
    # For empty or singleton lists, return immediately
    if len(arr) <= 1:
        return arr.copy()
        
    return _random_sort_impl(arr, max_attempts, 0)

def _random_sort_impl(arr: List[T], max_attempts: int, current_attempt: int) -> List[T]:
    """
    Internal implementation of the random sort with attempt counting.
    
    Args:
        arr: The list to sort
        max_attempts: Maximum number of attempts before falling back to built-in sort
        current_attempt: Current attempt number
        
    Returns:
        The sorted list
    """
    # If we've reached the max attempts, use the built-in sort as a fallback
    if current_attempt >= max_attempts:
        print(f"Giving up after {max_attempts} attempts. Using built-in sort instead.")
        return sorted(arr)
    
    # Create a copy of the list to avoid modifying the original
    working_arr = arr.copy()
    
    # Shuffle the list
    random.shuffle(working_arr)
    
    # Check if it's sorted
    if is_sorted(working_arr):
        return working_arr
    else:
        # If not sorted, recursively call again with incremented attempt counter
        return _random_sort_impl(arr, max_attempts, current_attempt + 1)

def is_sorted(arr: List[T]) -> bool:
    """
    Checks if a list is sorted.
    
    Args:
        arr: The list to check
        
    Returns:
        True if the list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) if len(arr) > 1 else True 