<<<<<<< HEAD
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
=======
from package.show import display
from package.write import plot

def write(snippet_name, password):
    return plot(snippet_name, password)
    

def show(snippet_name, password, clipboard=None):
    return display(snippet_name, password, clipboard=None)
>>>>>>> 5942f2ffc4482536c7b6feff21c1893134fdf31f
