from package.show import display
from package.write import plot


def write(snippet_name, password):
    try:
        return plot(snippet_name, password)
    except Exception as e:
        print(f"Error writing snippet: {e}")
        return None


def show(snippet_name, password, clipboard=None):
    try:
        return display(snippet_name, password, clipboard)
    except Exception as e:
        print(f"Error displaying snippet: {e}")
        return None
