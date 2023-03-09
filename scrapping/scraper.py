import os
import csv
import requests
from bs4 import BeautifulSoup

# Get the path to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))


url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    if table is not None:
        tbody = table.find('tbody')

        if tbody is not None:
            rows = tbody.find_all('tr')
            header_row = rows[0]
            headers = [header.text.strip() for header in header_row.find_all('th')[:-1]]

            # Create the file if it doesn't exist
            file_path = os.path.join(current_dir, '../data/highest_grossing_indian_films.csv')
            if not os.path.isfile(file_path):
                with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(headers)

            with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([col.text.strip() for col in row.find_all('td')][:8] for row in rows[1:])
        else:
            print("Table body element not found in HTML document")
            print(soup.prettify())
    else:
        print("Table element not found in HTML document")
        print(soup.prettify())
else:
    print(f"Failed to fetch page: {url}")
