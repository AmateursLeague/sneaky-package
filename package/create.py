import asyncio
import requests
import time

async def create(url_id, text, lifetime='60s'):
    base_url = 'https://cl1p.net'
    lifetime_seconds = convert_lifetime_to_seconds(lifetime)

    async def create_clip():
        url = f'{base_url}/{url_id}'
        data = {'content': text}
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
        print(f"Clip created successfully: https://cl1p.net/{url_id}")
    else:
        print("Failed to create the clip.")

def convert_lifetime_to_seconds(lifetime):
    parts = lifetime.split()
    if len(parts) != 2:
        raise ValueError("Lifetime must be in the format '<number> <unit>' (e.g., '1 day').")
    
    value, unit = parts
    try:
        value = int(value)
    except ValueError:
        raise ValueError("The first part of lifetime must be an integer.")

    if 'second' in unit or 'seconds' in unit:
        return value
    elif 'minute' in unit or 'minutes' in unit:
        return value * 60
    elif 'hour' in unit or 'hours' in unit:
        return value * 3600
    elif 'day' in unit or 'days' in unit:
        return value * 86400
    elif 'week' in unit or 'weeks' in unit:
        return value * 604800
    else:
        raise ValueError("Invalid time unit provided. Use seconds, minutes, hours, days, or weeks.")

if __name__ == "__main__":
    asyncio.run(create('yash1', 'This clip will self-destruct!', '1 day'))  # Example usage
