import os


def plot(snippet_name):
    snippet_path = os.path.join(os.path.dirname(__file__), 'code_snippets', f'{snippet_name}.py')
    output_path = os.path.join(os.path.dirname(__file__), f'{snippet_name}.py')
    with open(snippet_path, 'r') as file:
        source_code = file.read()
    with open(output_path, 'w') as output_file:
        output_file.write(source_code)
