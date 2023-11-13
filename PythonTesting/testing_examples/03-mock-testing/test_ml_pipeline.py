import os
import pytest
import shutil
from unittest import mock

from ml_save_pipeline import Dumper


@pytest.fixture()
def dump_folder():
    os.makedirs('test_dumps')

    yield 'test_dumps'

    shutil.rmtree('test_dumps')


@mock.patch('ml_save_pipeline.Dumper.get_checkpoints_folder', return_value='test_dumps')
def test_dump_worker(mock_dump_fn, dump_folder):
    dumper = Dumper()
    dumper.train_model(1)

    assert os.path.exists(os.path.join('test_dumps', '0'))


@mock.patch('ml_save_pipeline.Dumper.dump')
def test_dump_num_calls(mock_dump_fn, dump_folder):
    dumper = Dumper()
    dumper.train_model(num_epochs=3)

    assert 3 == mock_dump_fn.call_count  # Check that function was called three times
