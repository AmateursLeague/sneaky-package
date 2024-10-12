import os
import pytest
import shutil
from package.models import display
from datetime import datetime

def test_display_success(monkeypatch):
    def mock_copyfile(src, dstn):
        pass
    monkeypatch.setattr(shutil,"copyfile",mock_copyfile)
    try: 
        current_time = datetime.now().strftime("%H%M")
        display("test", current_time)
    except Exception as e:
        pytest.fail("Unexpected Error raised: {e}")

# will work on later
# due to some imposter uploaded write operations into models now this chaos has unfolded
# def test_display_failed(monkeypatch):
#     def mock_copyfile(src,dstn):
#         raise IOError("File not found")
#     monkeypatch.setattr(shutil,"copyfile",mock_copyfile)

#     with pytest.raises(IOError) as excinfo:
#         current_time = f"{int(datetime.now().strftime('%H%M')) + 1:04d}"
#         display("test", current_time)
#     assert "File not found" in str(excinfo.value)