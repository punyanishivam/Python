import requests
import datetime
from requests_html import HTML

now = datetime.datetime.now()
year = now.year


def url_to_file(url):

    r = requests.get(url)

    if r.status_code == 200:
        html_text = r.text
        return html_text
    return ""


url = "https://www.boxofficemojo.com/year/world/"

txt = url_to_file(url)

r_html = HTML(html=txt)

table_class = ".imdb-scroll-table"

r_table = r_html.find(table_class)

if len(r_table) == 1:
    parsed_table = r_table[0]
    rows = parsed_table.find('tr')
    header = rows[0]
    for row in rows[1:]:
        print(row.text)
        cols = row.find('td')
        for i, x in enumerate(cols):
            print(i, x.text, '\n\n')
