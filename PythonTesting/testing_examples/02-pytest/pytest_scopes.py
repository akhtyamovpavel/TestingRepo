import os
import shutil
import tempfile

import pytest

from TreeOpener import TreeOpener


@pytest.fixture(scope='module')
def folders():
    folder_path = tempfile.mkdtemp()
    os.makedirs(os.path.join(folder_path, 'assets_test_1'), exist_ok=True)
    file, filename = tempfile.mkstemp(dir=os.path.join(folder_path, 'assets_test_1'))
    os.close(file)
    yield {
        'folder_path': folder_path,
        'first_test_name': filename
    }
    shutil.rmtree(folder_path)
    assert not os.path.exists(folder_path)


def test_setup(folders):
    tree_opener: TreeOpener = TreeOpener(folders['folder_path'], with_dir=True)
    assert [
        folders['folder_path'],
        os.path.join(folders['folder_path'], 'assets_test_1'),
        folders['first_test_name']
    ] == tree_opener.run()
