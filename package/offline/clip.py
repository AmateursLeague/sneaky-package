import os
from package.offline.support import copy_to_clipboard
from package.offline.support import display


def clip(snippet_name, password):
    display(snippet_name, password, action="copy")
