import os
from package.offline.support import list_snippets, display
from package.password import valid_password

def show(snippet_name=None, password=None):
    if snippet_name is None and password is None:
        base_dir = os.path.dirname(__file__)
        snippets_dir = os.path.join(base_dir, "stash")
        list_snippets(snippets_dir)
        return

    display(snippet_name, password, action="display")