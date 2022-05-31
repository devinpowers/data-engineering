

import unittest

from insert_sort import insertion_sort

'''
Unit testing!!!!!!!
'''
class inserttests(unittest.TestCase):

     def test_insertion_sort(self):
        # Test with basic set of integers.
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12, -4, 3]
        result = data
        insertion_sort(result)
        expected = sorted(data) # using built in libary 'sorted'

        assert result == expected

        # Test with basic set of strings.
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence", "devin"]
        result = data
        insertion_sort(result)
        expected = sorted(data)
        
        assert result == expected

        # Test with already sorted data.
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = data
        insertion_sort(result)
        expected = data

        assert result == expected

        # Test empty.
        data = []
        result = data
        insertion_sort(result)
        expected = []

        assert result == expected

        # Check that function does not return anything!!!!
        data = [5, 6, 3, 2]
        result = insertion_sort(data)
        expected = None

        assert result == expected


if __name__ == '__main__':
    '''Run Main!!!'''
    unittest.main()

