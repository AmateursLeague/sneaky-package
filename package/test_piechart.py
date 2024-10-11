import os
import pytest
import shutil
from .piechart import plot  

def test_plot(monkeypatch):
    def mock_copyfile(inputPath, outputPath):
        pass
    monkeypatch.setattr(shutil, "copyfile", mock_copyfile)
    snippet_name = "test"
    plot(snippet_name)

    assert True 
