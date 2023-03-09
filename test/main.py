# from streamlit_app.app import MyApp
# import tracemalloc
# import asyncio
# import os
# from data.buildcsv import create_csv_file
#
# tracemalloc.start()
#
# if __name__ == '__main__':
#     csv_file_path = './data/highest_grossing_indian_films.csv'
#     if not os.path.exists(csv_file_path):
#         print(f"File not found at {csv_file_path}.")
#         create_csv_file(csv_file_path)
#         # handle the exception as per your requirement
#     else:
#         app = MyApp()
#         asyncio.run(app.run())

import asyncio
import os.path
from data.buildcsv import create_csv_file

csv_file_path = './data/highest_grossing_indian_films.csv'


async def main():
    await create_csv_file(csv_file_path)


asyncio.run(main())

from streamlit_app.app import MyApp

app = MyApp()
asyncio.run(app.run())
