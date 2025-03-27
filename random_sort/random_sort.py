import random
import sys
import time
from typing import List, TypeVar, Optional, Callable, Any

T = TypeVar('T')

def random_sort(arr: List[T], max_attempts: int = None, 
                verbose: bool = False, 
                key: Optional[Callable[[T], Any]] = None) -> List[T]:
    """
    Sorts a list by randomly shuffling it until it happens to be sorted.
    
    Args:
        arr: The list to sort
        max_attempts: Maximum number of attempts before giving up and using 
                     a deterministic sort (default: uses sys.getrecursionlimit())
        verbose: If True, prints progress information
        key: A function that extracts a comparison key from each element
             (similar to the key parameter in Python's sorted() function)
        
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
        
    return _random_sort_impl(arr, max_attempts, 0, verbose, key)

def _random_sort_impl(arr: List[T], max_attempts: int, current_attempt: int, 
                      verbose: bool, key: Optional[Callable[[T], Any]]) -> List[T]:
    """
    Internal implementation of the random sort with attempt counting.
    
    Args:
        arr: The list to sort
        max_attempts: Maximum number of attempts before falling back to built-in sort
        current_attempt: Current attempt number
        verbose: If True, prints progress information
        key: A function that extracts a comparison key from each element
        
    Returns:
        The sorted list
    """
    # Early termination for long lists
    if len(arr) > 10 and current_attempt > 5:
        if verbose:
            print(f"List length {len(arr)} is too large for efficient random sorting. "
                  f"Using built-in sort after {current_attempt} attempts.")
        return sorted(arr, key=key)
    
    # If we've reached the max attempts, use the built-in sort as a fallback
    if current_attempt >= max_attempts:
        if verbose:
            print(f"Giving up after {max_attempts} attempts. Using built-in sort instead.")
        return sorted(arr, key=key)
    
    # Create a copy of the list to avoid modifying the original
    working_arr = arr.copy()
    
    # Shuffle the list
    random.shuffle(working_arr)
    
    # Track time for verbose mode
    start_time = time.time() if verbose else None
    
    # Check if it's sorted
    if is_sorted(working_arr, key=key):
        if verbose:
            if start_time:
                print(f"Successfully sorted in {current_attempt + 1} attempts "
                      f"({time.time() - start_time:.6f} seconds).")
        return working_arr
    else:
        # Progress reporting in verbose mode
        if verbose and current_attempt % 10 == 0 and current_attempt > 0:
            print(f"Still trying to sort randomly... Attempt {current_attempt + 1}/{max_attempts}")
            
        # If not sorted, recursively call again with incremented attempt counter
        return _random_sort_impl(arr, max_attempts, current_attempt + 1, verbose, key)

def is_sorted(arr: List[T], key: Optional[Callable[[T], Any]] = None) -> bool:
    """
    Checks if a list is sorted.
    
    Args:
        arr: The list to check
        key: A function that extracts a comparison key from each element
        
    Returns:
        True if the list is sorted, False otherwise
    """
    if len(arr) <= 1:
        return True
        
    if key is None:
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    else:
        return all(key(arr[i]) <= key(arr[i+1]) for i in range(len(arr)-1))

def bogosort(arr: List[T], max_attempts: int = None, 
             verbose: bool = False,
             key: Optional[Callable[[T], Any]] = None) -> List[T]:
    """
    Alias for random_sort - implements the classic "bogosort" algorithm.
    
    Args:
        arr: The list to sort
        max_attempts: Maximum number of attempts before giving up and using 
                     a deterministic sort (default: uses sys.getrecursionlimit())
        verbose: If True, prints progress information
        key: A function that extracts a comparison key from each element
        
    Returns:
        The sorted list
    """
    return random_sort(arr, max_attempts, verbose, key) 