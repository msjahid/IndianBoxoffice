import csv
import requests
from bs4 import BeautifulSoup

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
            with open('../data/highest_grossing_indian_films.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                writer.writerows([col.text.strip() for col in row.find_all('td')][:8] for row in rows[1:])
                # writer.writerow(['Rank', 'Peak', 'Film', 'Year', 'Director', 'Studio(s)', 'Primary language',
                # 'Worldwide gross'])
                # for row in rows[1:]:
                #     columns = row.find_all('td')
                #     rank = columns[0].text.strip()
                #     peak = columns[1].text.strip()
                #     title = columns[2].text.strip()
                #     year = columns[3].text.strip()
                #     director = columns[4].text.strip()
                #     studio = columns[5].text.strip()
                #     language = columns[6].text.strip()
                #     worldwide_gross = columns[7].text.strip()
                #     writer.writerow([rank, peak, title, year, director, studio, language, worldwide_gross])
        else:
            print("Table body element not found in HTML document")
            print(soup.prettify())
    else:
        print("Table element not found in HTML document")
        print(soup.prettify())
else:
    print(f"Failed to fetch page: {url}")
