"""
This tests will test the response codes for the page
"""

import pytest
from flask import Response
from pytest_mock import mocker

from main import app
import main


@pytest.fixture(scope='session')
def flask_app():
    return app


def test_string_name(flask_app):
    response = flask_app.test_client().get('/pavel/')
    assert response.status_code == 200


def test_uncorrect_index_id(flask_app):
    response = flask_app.test_client().get('/integer/5/')
    assert response.status_code == 200


def test_uncorrect_index_string(flask_app):
    response = flask_app.test_client().get('/integer/pavel/')
    assert response.status_code == 404


def test_button_click_correctly(mocker, flask_app):
    mocker.patch.object(main, 'db_connection_usage')
    main.db_connection_usage.return_value = '120'

    response: Response = flask_app.test_client().post('/button_click')
    # response.data
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '120'
    assert main.db_connection_usage.call_count == 1
    assert main.db_connection_usage.called

