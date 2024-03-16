import os
import inspect
import ctypes

def display(snippet_name):
    snippet_path = os.path.join(os.path.dirname(__file__), 'code_snippets', f'{snippet_name}.py')

    with open(snippet_path, 'r') as file:
        source_code = file.read()

    # Attempt to copy the source code to the clipboard
    try:
        copy_to_clipboard(source_code)
        print("Source code copied to clipboard.")
    except Exception as e:
        print("Error copying to clipboard:", e)

def copy_to_clipboard(text):
    user32 = ctypes.WinDLL('user32')
    kernel32 = ctypes.WinDLL('kernel32')

    GMEM_MOVEABLE = 0x0002
    CF_UNICODETEXT = 13

    kernel32.GlobalAlloc.restype = ctypes.wintypes.HGLOBAL
    kernel32.GlobalLock.argtypes = [ctypes.wintypes.HGLOBAL]
    kernel32.GlobalUnlock.argtypes = [ctypes.wintypes.HGLOBAL]
    kernel32.GlobalSize.argtypes = [ctypes.wintypes.HGLOBAL]
    user32.SetClipboardData.argtypes = [ctypes.wintypes.UINT, ctypes.wintypes.HANDLE]

    data = text.encode('utf-16le')
    size = len(data)

    handle = kernel32.GlobalAlloc(GMEM_MOVEABLE, size)
    if handle:
        ptr = kernel32.GlobalLock(handle)
        ctypes.memmove(ptr, ctypes.c_char_p(data), size)
        kernel32.GlobalUnlock(handle)
        user32.OpenClipboard(0)
        user32.EmptyClipboard()
        user32.SetClipboardData(CF_UNICODETEXT, handle)
        user32.CloseClipboard()
    else:
        raise ctypes.WinError()

# Example usage:
# display('your_snippet_name')
