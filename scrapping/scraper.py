import os
import csv
import io
from github import Github
from bs4 import BeautifulSoup
import requests

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
try:
    contents = repo.get_contents(file_path)

except:
    repo.create_file(file_path, "create file", "")
    contents = repo.get_contents(file_path)

# Fetch the CSV data
response = requests.get(csv_url)

if response.status_code == 200:
    csv_data = response.content.decode('utf-8').splitlines()

    # Parse the CSV data
    csv_reader = csv.reader(csv_data, delimiter=',')
    headers = next(csv_reader)

    # Create the CSV writer object
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer, delimiter=',')

    # Write the header row to the CSV buffer
    csv_writer.writerow(headers)

    # Write the data rows to the CSV buffer
    for row in csv_reader:
        csv_writer.writerow(row)

    # Commit the changes to GitHub
    repo.update_file(file_path, "refresh data", csv_buffer.getvalue(), contents.sha)
else:
    print(f"Failed to fetch CSV file: {csv_url}")
