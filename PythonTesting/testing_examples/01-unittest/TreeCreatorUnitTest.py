import os
import shutil
import unittest

import tempfile

from TreeOpener import TreeOpener


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder_path = tempfile.mkdtemp()
        print(cls.folder_path)
        os.makedirs(os.path.join(cls.folder_path, 'assets_test_1'), exist_ok=True)
        file, filename = tempfile.mkstemp(dir=os.path.join(cls.folder_path, 'assets_test_1'))
        os.close(file)
        cls.first_test_name = filename

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.folder_path)

    def test_setup(self):
        tree_opener: TreeOpener = TreeOpener(self.folder_path, with_dir=True)
        self.assertEqual(
            tree_opener.run(), [
                self.folder_path,
                os.path.join(self.folder_path, 'assets_test_1'),
                self.first_test_name
            ]
        )


if __name__ == '__main__':
    unittest.main()
