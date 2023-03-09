import os.path
import subprocess
import sys
import asyncio


async def create_csv_file(csv_file_path):
    print(f"Creating CSV file: {csv_file_path}")
    if not os.path.exists(csv_file_path):
        cmd = ["python3", "scrapping/scraper.py"]
        process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            print(f"Error creating CSV file: {stderr.decode('utf-8')}")
        else:
            print(f"CSV file created successfully: {csv_file_path}")
    else:
        print(f"CSV file already exists: {csv_file_path}")
