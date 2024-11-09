import os
import pytest
from unittest.mock import patch, mock_open
from package.offline.support import display
from package.offline.clip import clip
from package.password import valid_password


def test_clip_invalid_password():
    snippet_name = "test_snippet.txt"
    password = "invalid_password" 

    with pytest.raises(ValueError, match="Incorrect password"):
        clip(snippet_name, password)
