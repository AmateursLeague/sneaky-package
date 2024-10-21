import asyncio
import requests

async def create(url_id, text, lifetime_seconds=60):
    base_url = 'https://cl1p.net'

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

    async def destroy_clip():
        url = f'{base_url}/{url_id}'
        data = {'content': '', 'delete': 'true'}
        try:
            response = await asyncio.to_thread(requests.post, url, data=data)
            if response.status_code == 200:
                return True
            else:
                print(f"Failed to destroy clip: Status code {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Failed to destroy clip: {e}")
            return False

    create_success = await create_clip()
    if create_success:
        print(f"Clip created successfully: https://cl1p.net/{url_id}")
        print(f"Clip will be destroyed in {lifetime_seconds} seconds.")
        
        await asyncio.sleep(lifetime_seconds)
        
        destroy_success = await destroy_clip()
        if destroy_success:
            print(f"Clip destroyed successfully after {lifetime_seconds} seconds.")
        else:
            print("Failed to destroy the clip.")
    else:
        print("Failed to create the clip.")

if __name__ == "__main__":
    asyncio.run(create('yash1', 'This clip will self-destruct!', 15))