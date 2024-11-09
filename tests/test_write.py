import pytest
import os
import shutil
from datetime import datetime
from unittest.mock import Mock
from package.offline.write import write


@pytest.fixture
def setup_test_env():
    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    os.makedirs(snippets_dir, exist_ok=True)

    test_file = "test_snippet.txt"
    test_content = "Test content"
    with open(os.path.join(snippets_dir, test_file), "w") as f:
        f.write(test_content)

    yield base_dir, snippets_dir, test_file, test_content

    if os.path.exists(snippets_dir):
        shutil.rmtree(snippets_dir)
    if os.path.exists(os.path.join(base_dir, test_file)):
        os.remove(os.path.join(base_dir, test_file))


@pytest.fixture
def mock_time(monkeypatch):
    mock_dt = Mock()
    mock_dt.now.return_value.strftime.return_value = "1430"
    monkeypatch.setattr("package.password.datetime", mock_dt)
    return mock_dt


def test_invalid_password_type(setup_test_env, mock_time):
    _, _, test_file, _ = setup_test_env
    with pytest.raises(ValueError):
        write(test_file, "1430")


def test_invalid_password_value(setup_test_env, mock_time):
    _, _, test_file, _ = setup_test_env

    with pytest.raises(ValueError):
        write(test_file, 1431)


def test_nonexistent_file(setup_test_env, mock_time):
    base_dir, _, _, _ = setup_test_env

    write("nonexistent.txt", 1430)
    assert not os.path.exists(os.path.join(base_dir, "nonexistent.txt"))


def test_copy_permission_error(setup_test_env, mock_time, monkeypatch):
    base_dir, _, test_file, _ = setup_test_env
    monkeypatch.setattr(
        "shutil.copyfile",
        lambda x, y: exec('raise PermissionError("Permission denied")'),
    )

    write(test_file, 1430)
    assert not os.path.exists(os.path.join(base_dir, test_file))
