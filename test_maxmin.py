import unittest
from main import maxmin_select

class TestMaxMinSelect(unittest.TestCase):
    def test_basic(self):
        arr = [3, 1, 4, 1, 5, 9]
        res = maxmin_select(arr)
        self.assertEqual(res.minimum, 1)
        self.assertEqual(res.maximum, 9)
        self.assertTrue(res.comparisons <= 2*len(arr)-2)

    def test_single(self):
        arr = [42]
        res = maxmin_select(arr)
        self.assertEqual(res.minimum, 42)
        self.assertEqual(res.maximum, 42)
        self.assertEqual(res.comparisons, 0)

if __name__ == "__main__":
    unittest.main()
