import os
import pytest
import shutil
from package.models import display

def test_display_success(monkeypatch):
    def mock_copyfile(src, dstn):
        pass
    monkeypatch.setattr(shutil,"copyfile",mock_copyfile)
    try: 
        display("test")
    except Exception as e:
        pytest.fail("Unexpected Error raised: {e}")


def test_display_failed(monkeypatch):
    def mock_copyfile(src,dstn):
        raise IOError("File not found")
    monkeypatch.setattr(shutil,"copyfile",mock_copyfile)

    with pytest.raises(IOError) as excinfo:
        display("test")
    assert "File not found" in str(excinfo.value)