import csv
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile

import requests

resp = requests.get('https://s3.amazonaws.com/alexa-static/top-1m.csv.zip', stream=True)
urls = []

with ZipFile(BytesIO(resp.content)) as zf:
    csv_filename = zf.namelist()[0]
    with zf.open(csv_filename) as csv_file:
        for _, website in csv.reader(TextIOWrapper(csv_file)):
            urls.append('https://' + website)

print(urls)