import unittest
import BubbleSort
import SortAlgorithmTestCase


class BubbleSortTest(SortAlgorithmTestCase.SortAlgorithmTestCase):

    def apply_sort(self, list_of_things):
        return BubbleSort.bubble_sort(list_of_things)


if __name__ == '__main__':
    unittest.main()
