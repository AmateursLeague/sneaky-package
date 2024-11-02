import asyncio
import requests
import subprocess
import platform


def get_clipboard_content() -> str:
    # Detect the operating system
    current_os = platform.system()

    try:
        if current_os == "Linux":
            # Use xclip to get clipboard content
            result = subprocess.run(
                ["xclip", "-selection", "clipboard", "-o"], stdout=subprocess.PIPE, check=True
            )
            return result.stdout.decode("utf-8")
        elif current_os == "Darwin":  # macOS
            # Use pbpaste to get clipboard content
            result = subprocess.run(["pbpaste"], stdout=subprocess.PIPE, check=True)
            return result.stdout.decode("utf-8")
        elif current_os == "Windows":
            # Use PowerShell to get clipboard content on Windows
            result = subprocess.run(
                ["powershell", "-command", "Get-Clipboard"], stdout=subprocess.PIPE, check=True
            )
            return result.stdout.decode("utf-8")
        else:
            print(f"Unsupported OS: {current_os}")
            return ""
    except subprocess.CalledProcessError:
        print("Failed to get clipboard content.")
        return ""


async def create(url_id, lifetime="60s"):
    text = get_clipboard_content()
    if not text:
        print("Clipboard is empty or could not be accessed.")
        return

    base_url = "https://cl1p.net"
    try:
        lifetime_seconds = convert_lifetime_to_seconds(lifetime)
    except ValueError as e:
        print(f"Invalid lifetime format: {e}")
        return

    url = f"{base_url}/{url_id}"
    data = {"content": text, "lifetime": lifetime_seconds}

    async def create_clip():
        try:
            response = await asyncio.to_thread(requests.post, url, data=data)
            if response.status_code == 200:
                return True
            else:
                print(f"Failed to create clip: Status code {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Failed to create clip: {e}")
            return False

    create_success = await create_clip()
    if create_success:
        print(f"Clip created successfully: {url}")
    else:
        print("Failed to create the clip.")


def convert_lifetime_to_seconds(lifetime):
    # Parse and convert lifetime to seconds
    if " " not in lifetime:
        lifetime = f"{lifetime[:-1]} {lifetime[-1]}"  # Handle no-space case

    parts = lifetime.split()
    if len(parts) != 2:
        raise ValueError("Lifetime must be in the format '<number> <unit>' (e.g., '1 day').")

    value, unit = parts
    try:
        value = int(value)
    except ValueError:
        raise ValueError("The first part of lifetime must be an integer.")

    unit = unit.lower()
    if "second" in unit:
        return value
    elif "minute" in unit:
        return value * 60
    elif "hour" in unit:
        return value * 3600
    elif "day" in unit:
        return value * 86400
    elif "week" in unit:
        return value * 604800
    else:
        raise ValueError("Invalid time unit provided. Use seconds, minutes, hours, days, or weeks.")


if __name__ == "__main__":
    asyncio.run(create("yash1", "1 day"))
