import asyncio
import os
from data.buildcsv import create_csv_file
from dotenv import load_dotenv
from github import Github

# Load environment variables from .env file
load_dotenv()

# Load the environment variables
csv_url = os.getenv('CSV_URL')
token = os.getenv('ACCESS_TOKEN')
user = os.getenv('USERNAME')
repo_name = os.getenv('REPOSITORY')

# Authenticate with GitHub
g = Github(token)

# Specify the repository details
repo = g.get_user(user).get_repo(repo_name)

# Get the contents of the file, or create a new file if it doesn't exist
file_path = "data/highest_grossing_indian_films.csv"
contents = None  # Set initial value to None


async def main():
    if not csv_url:
        print(f"File not found at {file_path}.")
        await create_csv_file(file_path)
    else:
        try:
            print(f"Please wait file refreshing.. {file_path}.")
            contents = repo.get_contents(file_path)  # Retrieve the latest contents
            await repo.delete_file(file_path, "update data", contents.sha)
        except Exception as e:
            print(f"Error deleting file: {e}")
        await create_csv_file(file_path)
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                await repo.create_file(file_path, "refresh data", content)
        except Exception as e:
            print(f"Error creating CSV file: {e}")


asyncio.run(main())

from streamlit_app.app import MyApp

if __name__ == '__main__':
    app = MyApp()
    asyncio.run(app.run())
