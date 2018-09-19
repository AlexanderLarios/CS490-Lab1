from bs4 import BeautifulSoup
import requests

# cache link
link = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
source_material = requests.get(link)

# convert saved website data as a text file
source_text = source_material.text

# parse with beautiful soup library
soup_response = BeautifulSoup(source_text, "html.parser")

# find the table
table = soup_response.find_all('table')

# output table to
file_out = open('table_out.txt', 'w')
file_out.write(str(table))