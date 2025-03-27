from random_sort import random_sort
import time

def main():
    print("Example of using random_sort")
    
    # A small list to sort
    print("\nSorting a small list:")
    small_list = [3, 1, 4, 1, 5]
    print(f"Original list: {small_list}")
    start_time = time.time()
    sorted_list = random_sort(small_list)
    elapsed_time = time.time() - start_time
    print(f"Sorted list: {sorted_list}")
    print(f"Time taken: {elapsed_time:.6f} seconds")
    
    # Try with a medium list
    print("\nSorting a medium list with max_attempts=20:")
    medium_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Original list: {medium_list}")
    start_time = time.time()
    sorted_list = random_sort(medium_list, max_attempts=20)
    elapsed_time = time.time() - start_time
    print(f"Sorted list: {sorted_list}")
    print(f"Time taken: {elapsed_time:.6f} seconds")
    
    # Try with a longer list but only a few attempts
    print("\nDo you want to try with a longer list? (y/n)")
    choice = input().lower()
    if choice == 'y':
        long_list = list(range(20, 0, -1))  # [20, 19, 18, ..., 1]
        print(f"Original list: {long_list}")
        print("Starting sorting with max_attempts=10...")
        start_time = time.time()
        sorted_list = random_sort(long_list, max_attempts=10)
        elapsed_time = time.time() - start_time
        print(f"Sorted list: {sorted_list}")
        print(f"Time taken: {elapsed_time:.6f} seconds")
    
if __name__ == "__main__":
    main() 