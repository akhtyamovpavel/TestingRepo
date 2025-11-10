import os
import shutil
import tempfile

import pytest

from TreeOpener import TreeOpener


@pytest.fixture(scope='module')
def folders():
    ## Setup
    folder_path = tempfile.mkdtemp()
    os.makedirs(os.path.join(folder_path, 'assets_test_1'), exist_ok=True)
    file, filename = tempfile.mkstemp(dir=os.path.join(folder_path, 'assets_test_1'))
    os.close(file)
    ## Setup ends here
    yield {
        'folder_path': folder_path,
        'first_test_name': filename
    }
    ## Teardown starts here
    shutil.rmtree(folder_path)
    ## Teardown ends here
    assert not os.path.exists(folder_path)


def test_setup(folders: dict[str, str]):
    tree_opener: TreeOpener = TreeOpener(folders['folder_path'], with_dir=True)
    assert [
        folders['folder_path'],
        os.path.join(folders['folder_path'], 'assets_test_1'),
        folders['first_test_name']
    ] == tree_opener.run()
