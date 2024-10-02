import subprocess
import sys


def display(snippet_name, source_code):
    def copy_to_clipboard(text):
        """
        Copies text to the system clipboard based on the platform.
        """
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
            raise FileNotFoundError("Clipboard utility not found.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error during clipboard copying: {e}")

    # Copy the source code to clipboard
    copy_to_clipboard(source_code)

    # Display the snippet's content
    print(f"Snippet Name: {snippet_name}\n")
    print(source_code)
