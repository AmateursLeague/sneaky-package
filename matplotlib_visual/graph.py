import os

# Operating system detection
if os.name == 'nt':  # Windows
    def copy_to_clipboard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)
elif os.name == 'posix':  # Linux or macOS
    def copy_to_clipboard(text):
        command = 'echo ' + text.strip() + '| xclip -selection clipboard'
        os.system(command)
else:
    raise OSError("Unsupported operating system")

def display(snippet_name):
    snippet_path = os.path.join(os.path.dirname(__file__), 'code_snippets', f'{snippet_name}.py')

    with open(snippet_path, 'r') as file:
        source_code = file.read()

    copy_to_clipboard(source_code)
