# Welcome to our Python asyncio playground!

import asyncio
import time

async def download_large_file(file_name: str):
    print(f"Current file before await: {file_name}")
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f"{file_name} was downloaded successfully")
    return f"{file_name}: OK"

FILES_TO_DOWNLOAD = [
    "textures.zip",
    "models.zip",
    "physics_engine.exe",
    "game.exe",
    "achievements.exe",
    "audio_pack.zip",
]

async def main():
    start_time = time.time()
    downloads = [download_large_file(file) for file in FILES_TO_DOWNLOAD]
    download_statuses = await asyncio.gather(*downloads)
    total_time = time.time() - start_time
    print(f"Finished Downloading {len(download_statuses)} files in {total_time:.2f} seconds!")

asyncio.run(main())
