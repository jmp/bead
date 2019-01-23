import unittest
import bead


class TestSort(unittest.TestCase):
    def test_smoke(self):
        self.assertTrue(callable(bead.sort))

    def test_sort_empty_list(self):
        self.assertEqual([], bead.sort([]))

    def test_sort_single_item(self):
        self.assertEqual([1], bead.sort([1]))

    def test_sort_invalid_items(self):
        self.assertRaises(ValueError, bead.sort, ['a'])
        self.assertRaises(ValueError, bead.sort, [1, 'a'])

    def test_sort_sorted(self):
        self.assertEqual([1, 2, 3], bead.sort([1, 2, 3]))

    def test_sort_reversed(self):
        self.assertEqual([1, 2, 3, 4, 5], bead.sort([5, 4, 3, 2, 1]))

    def test_sort_repeating(self):
        self.assertEqual([1, 2, 2, 2, 5, 5, 6], bead.sort([6, 5, 2, 5, 2, 2, 1]))

    def test_sort_with_zero(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], bead.sort([1, 4, 0, 5, 2, 3]))


class TestCreateBeads(unittest.TestCase):
    def test_create_beads_simple(self):
        self.assertEqual([
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1],
        ], bead.create_beads([1, 2, 3]))

    def test_create_beads_shuffled(self):
        self.assertEqual([
            [1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
        ], bead.create_beads([5, 2, 1, 4, 4]))


class TestDropBeads(unittest.TestCase):
    def test_drop_beads(self):
        input_beads = [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
        ]
        expected_output = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
        ]
        self.assertListEqual(expected_output, bead.drop_beads(input_beads))
