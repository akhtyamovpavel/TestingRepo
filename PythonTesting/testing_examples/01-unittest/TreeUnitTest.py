import os
import unittest

from TreeOpener import TreeOpener


class TreeUnitTest(unittest.TestCase):
    def test_tree_opener(self):
        tree_opener: TreeOpener = TreeOpener('assets')
        self.assertSequenceEqual([
            os.path.join('assets', '1.txt')
        ], tree_opener.run())

    def test_dir_opener(self):
        tree_opener: TreeOpener = TreeOpener('assets', with_dir=True)
        self.assertSequenceEqual([
            'assets',
            os.path.join('assets', '1.txt')
        ], tree_opener.run())

    def test_depths_two(self):
        tree_opener: TreeOpener = TreeOpener('assets_multiple', with_dir=True)
        self.assertSequenceEqual([
            'assets_multiple',
            os.path.join('assets_multiple', 'assets'),
            os.path.join('assets_multiple', 'assets', '1.txt')
        ], tree_opener.run())

    def test_not_directory(self):
        tree_opener: TreeOpener = TreeOpener('1.txt')
        self.assertRaises(ValueError, tree_opener.run)


if __name__ == '__main__':
    unittest.main()
