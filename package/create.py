import asyncio
import requests

async def create(url_id, text, lifetime_seconds=60):
    base_url = 'https://cl1p.net'

    async def create_clip():
        url = f'{base_url}/{url_id}'
        data = {'content': text}
        response = await asyncio.to_thread(requests.post, url, data=data)
        return response.status_code == 200

    async def destroy_clip():
        url = f'{base_url}/{url_id}'
        data = {'content': '', 'delete': 'true'}
        response = await asyncio.to_thread(requests.post, url, data=data)
        return response.status_code == 200

    # Create the clip
    create_success = await create_clip()
    if create_success:
        print(f"Clip created successfully: https://cl1p.net/{url_id}")
        print(f"Clip will be destroyed in {lifetime_seconds} seconds.")
        
        # Wait for the specified lifetime
        await asyncio.sleep(lifetime_seconds)
        
        # Destroy the clip
        destroy_success = await destroy_clip()
        if destroy_success:
            print(f"Clip destroyed successfully after {lifetime_seconds} seconds.")
        else:
            print("Failed to destroy the clip.")
    else:
        print("Failed to create the clip.")



asyncio.run(create('yash1', 'This clip will self-destruct!', 15))