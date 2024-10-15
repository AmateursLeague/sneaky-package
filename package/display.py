from package.show import display
from package.write import plot

def display(method, snippet_name, password, clipboard=None):
    if method == "show":
        display(snippet_name, password, clipboard)
    elif method == "write":
        write_plot(snippet_name, password)
    else:
        raise ValueError(f"Unknown method '{method}' specified. Valid methods are 'clip', 'show', or 'write'.")

def write_plot(snippet_name, password):
    return plot(snippet_name, password)
    

def show(snippet_name, password, clipboard=None):
    return display(snippet_name, password, clipboard=None)
