import os

import pytest

from TreeOpener import TreeOpener


def test_tree_opener():
    tree_opener: TreeOpener = TreeOpener('assets')
    assert [
        os.path.join('assets', '1.txt')
    ] == tree_opener.run()


def test_dir_opener():
    tree_opener: TreeOpener = TreeOpener('assets', with_dir=True)
    assert [
        'assets',
        os.path.join('assets', '1.txt')
    ] == tree_opener.run()


def test_depths_two():
    tree_opener: TreeOpener = TreeOpener('assets_multiple', with_dir=True)
    assert [
        'assets_multiple',
        os.path.join('assets_multiple', 'assets'),
        os.path.join('assets_multiple', 'assets', '1.txt')
    ] == tree_opener.run()


def test_not_directory():
    tree_opener: TreeOpener = TreeOpener('1.txt')
    pytest.raises(ValueError, tree_opener.run)
