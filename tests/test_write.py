import shutil
import glob
from datetime import datetime
from package.write import plot


# Mocking the datetime class
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime.strptime("1234", "%H%M")  # Mock time to 12:34


def mock_copyfile(src, dst):
    pass  # Mock copyfile to do nothing


def mock_glob_single(pattern):
    return ["stash/test.py"]  # Return a single mock file


def mock_glob_none(pattern):
    return []  # Return no files found


def mock_glob_multiple(pattern):
    return ["stash/test.py", "stash/test2.py"]  # Return multiple mock files


def test_plot_success(monkeypatch, capfd):
    monkeypatch.setattr("package.write.datetime", MockDateTime)
    monkeypatch.setattr(shutil, "copyfile", mock_copyfile)
    monkeypatch.setattr(glob, "glob", mock_glob_single)

    snippet_name = "test"
    password = "1234"
    plot(snippet_name, password)

    # Verify output
    captured = capfd.readouterr()
    assert "File 'stash/test.py' copied successfully" in captured.out


def test_plot_no_file_found(monkeypatch, capfd):
    monkeypatch.setattr("package.write.datetime", MockDateTime)
    monkeypatch.setattr(glob, "glob", mock_glob_none)

    snippet_name = "nonexistent"
    password = "1234"
    plot(snippet_name, password)

    # Verify output
    captured = capfd.readouterr()
    assert "File is not found" in captured.out


def test_plot_multiple_files_found(monkeypatch, capfd):
    monkeypatch.setattr("package.write.datetime", MockDateTime)
    monkeypatch.setattr(glob, "glob", mock_glob_multiple)

    snippet_name = "test"
    password = "1234"
    plot(snippet_name, password)

    # Verify output
    captured = capfd.readouterr()
    assert "The given values are not supported" in captured.out
