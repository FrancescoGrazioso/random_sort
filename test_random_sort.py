import unittest
from random_sort import random_sort

class TestRandomSort(unittest.TestCase):
    
    def test_empty_list(self):
        """Verify that an empty list remains empty."""
        self.assertEqual(random_sort([]), [])
    
    def test_single_element(self):
        """Verify that a list with a single element remains unchanged."""
        self.assertEqual(random_sort([42]), [42])
    
    def test_sorted_result(self):
        """Verify that the result is actually sorted."""
        input_list = [3, 1, 4, 1, 5, 9, 2, 6]
        # Use a reasonable max_attempts to avoid test failures due to randomness
        result = random_sort(input_list, max_attempts=50)
        
        # Verify that the result is sorted
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])
        
        # Verify that all original elements are present
        self.assertEqual(sorted(input_list), result)
    
    def test_already_sorted(self):
        """Verify that an already sorted list remains unchanged."""
        sorted_list = [1, 2, 3, 4, 5]
        result = random_sort(sorted_list)
        self.assertEqual(result, sorted_list)
        
    def test_max_attempts_fallback(self):
        """Verify that the function falls back to built-in sort after max attempts."""
        # A list that's unlikely to be sorted randomly in just one attempt
        long_list = list(range(15, 0, -1))  # [15, 14, 13, ..., 1]
        
        # Set max_attempts to 1 to force fallback
        result = random_sort(long_list, max_attempts=1)
        
        # The result should be the same as using the built-in sort
        self.assertEqual(result, sorted(long_list))

if __name__ == '__main__':
    unittest.main() 