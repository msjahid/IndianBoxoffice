import asyncio
import os.path
from data.buildcsv import create_csv_file

csv_file_path = './data/highest_grossing_indian_films.csv'


async def main():
    if not os.path.exists(csv_file_path):
        print(f"File not found at {csv_file_path}.")
        await create_csv_file(csv_file_path)
    else:
        try:
            print(f"Please wait file refreshing.. {csv_file_path}.")
            os.remove(csv_file_path)
        except FileNotFoundError:
            pass
        await create_csv_file(csv_file_path)


asyncio.run(main())

from streamlit_app.app import MyApp

if __name__ == '__main__':
    app = MyApp()
    asyncio.run(app.run())