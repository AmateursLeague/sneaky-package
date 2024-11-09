import os
from package.offline.support.copy_to_clipboard import copy_to_clipboard
from package.offline.support.display import display


def clip(snippet_name, password):
    display(snippet_name, password, action="copy")
