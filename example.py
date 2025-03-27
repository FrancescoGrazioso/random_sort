from random_sort import random_sort, bogosort
import time

def main():
    print("Example of using random_sort")
    
    # A small list to sort
    print("\n1. Sorting a small list:")
    small_list = [3, 1, 4, 1, 5]
    print(f"Original list: {small_list}")
    start_time = time.time()
    sorted_list = random_sort(small_list)
    elapsed_time = time.time() - start_time
    print(f"Sorted list: {sorted_list}")
    print(f"Time taken: {elapsed_time:.6f} seconds")
    
    # Try with a medium list and verbose output
    print("\n2. Sorting a medium list with verbose output:")
    medium_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Original list: {medium_list}")
    sorted_list = random_sort(medium_list, max_attempts=20, verbose=True)
    print(f"Sorted list: {sorted_list}")
    
    # Demonstrate using bogosort alias
    print("\n3. Using the bogosort alias:")
    small_list_2 = [5, 3, 1, 2, 4]
    print(f"Original list: {small_list_2}")
    sorted_list = bogosort(small_list_2, verbose=True)
    print(f"Sorted list: {sorted_list}")
    
    # Demonstrate using key function
    print("\n4. Sorting with a key function:")
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    print(f"Original list: {people}")
    sorted_people = random_sort(people, key=lambda x: x["age"], verbose=True)
    print(f"Sorted list by age: {sorted_people}")
    
    # Try with a longer list
    print("\n5. Do you want to try with a longer list? (y/n)")
    choice = input().lower()
    if choice == 'y':
        long_list = list(range(20, 0, -1))  # [20, 19, 18, ..., 1]
        print(f"Original list: {long_list}")
        print("Starting sorting with max_attempts=10...")
        sorted_list = random_sort(long_list, max_attempts=10, verbose=True)
        print(f"Sorted list: {sorted_list}")
    
if __name__ == "__main__":
    main() 