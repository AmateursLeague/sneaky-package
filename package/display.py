from package.clip import display as clip_display
from package.show import display as show_display
from package.write import plot as write_plot

def display(method, snippet_name, password, clipboard=None):
    if method == "clip":
        clip_display(snippet_name, password)
    elif method == "show":
        show_display(snippet_name, password, clipboard)
    elif method == "write":
        write_plot(snippet_name, password)
    else:
        raise ValueError(f"Unknown method '{method}' specified. Valid methods are 'clip', 'show', or 'write'.")
