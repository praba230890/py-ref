from insertionsort import insertion_sort
import unittest

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.a = [1,7,8,3,9,4,2]
        self.a_sorted = [1,2,3,4,7,8,9]
        self.b = [10,7,4,9,1]
        self.b_sorted = [1,4,7,9,10]
        self.c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1]
        self.d_sorted = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    def test_insertion_sort(self):
        self.assertEqual(self.a_sorted, insertion_sort(self.a))
        self.assertEqual(self.b_sorted, insertion_sort(self.b))
        self.assertEqual(self.c, insertion_sort(self.c))
        self.assertEqual(self.d_sorted, insertion_sort(self.d))

if __name__ == '__main__':
    unittest.main()
