import unittest
import io
import sys
from random_sort import random_sort, bogosort

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
    
    def test_verbose_output(self):
        """Test that verbose mode produces output."""
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Call the function with verbose=True
            long_list = list(range(10, 0, -1))
            random_sort(long_list, max_attempts=2, verbose=True)
            
            # Check that something was printed
            output = captured_output.getvalue()
            self.assertGreater(len(output), 0)
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__
    
    def test_key_function(self):
        """Test sorting with a key function."""
        people = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35}
        ]
        
        # Sort by age using built-in sort for comparison
        expected = sorted(people, key=lambda x: x["age"])
        
        # Force using built-in sort by setting max_attempts to 1
        result = random_sort(people, key=lambda x: x["age"], max_attempts=1)
        
        # The ages should be in ascending order
        self.assertEqual(result, expected)
    
    def test_bogosort_alias(self):
        """Test that bogosort function is an alias for random_sort."""
        test_list = [3, 2, 1]
        # Use a fixed seed or max_attempts to ensure deterministic behavior
        result1 = random_sort(test_list, max_attempts=1)
        result2 = bogosort(test_list, max_attempts=1)
        
        # Both functions should produce the same result
        self.assertEqual(result1, result2)
        
    def test_early_termination_for_long_lists(self):
        """Test early termination for lists longer than 10 elements."""
        long_list = list(range(20, 0, -1))  # [20, 19, 18, ..., 1]
        
        # Capture stdout to verify the early termination message
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Set max_attempts high, but it should terminate early
            result = random_sort(long_list, max_attempts=100, verbose=True)
            
            # Check that the early termination message was printed
            output = captured_output.getvalue()
            self.assertIn("List length", output)
            self.assertIn("is too large for efficient random sorting", output)
            
            # The result should be correctly sorted
            self.assertEqual(result, sorted(long_list))
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main() 