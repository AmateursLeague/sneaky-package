import subprocess
import sys


def display(snippet_name, source_code):
    """
    Display the snippet's content and copy it to the clipboard.

    Args:
        snippet_name (str): The name of the snippet.
        source_code (str): The source code to be copied and displayed.
    """

    def copy_to_clipboard(text):
        try:
            # Linux
            if "linux" in sys.platform:
                subprocess.run(
                    ["/usr/bin/xclip", "-selection", "clipboard"],
                    input=text.strip().encode(),
                    check=True,
                )

            # Windows
            elif "win32" in sys.platform:
                subprocess.run(
                    ["C:\\Windows\\System32\\clip.exe"],
                    input=text.strip().encode(),
                    check=True,
                )

            # macOS
            elif "darwin" in sys.platform:
                subprocess.run(
                    ["/usr/bin/pbcopy"],  # Full path to pbcopy for macOS
                    input=text.strip().encode(),
                    check=True,
                )

            else:
                raise OSError("Unsupported operating system")

        except FileNotFoundError:
            print("Error: Clipboard utility not found. Cannot copy to clipboard.")
        except subprocess.CalledProcessError as e:
            print(f"Error during clipboard copying: {e}")

    # Copy the source code to clipboard
    copy_to_clipboard(source_code)

    # Display the snippet's content
    print(f"Snippet Name: {snippet_name}\n")
    print(source_code)


# Example usage
if __name__ == "__main__":
    example_name = "Sample Code Snippet"
    example_code = """print("Hello, World!")"""
    display(example_name, example_code)
