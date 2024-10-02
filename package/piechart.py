import os

def plot(snippet_name):
    # Define paths for the source snippet and output file
    snippet_path = os.path.join(os.path.dirname(__file__), "stash", f"{snippet_name}.py")
    output_path = os.path.join(os.path.dirname(__file__), f"{snippet_name}.py")
    
    # Check if the snippet file exists in the 'stash' directory
    if os.path.isfile(snippet_path):
        # If it exists, read the file and write its contents to the output path
        with open(snippet_path, "r") as file:
            source_code = file.read()
        with open(output_path, "w") as output_file:
            output_file.write(source_code)
    else:
        # Minimal error message 
        print("Check for syntax errors.")
