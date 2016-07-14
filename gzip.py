#! python3

import gzip
from urllib.request import urlopen
data_url = "https://httpbin.org/gzip"
with urlopen(data_url) as response:
    with gzip.GzipFile(fileobj=response, mode='rb') as extracted:
        with open('data.txt', mode='wb') as data_file:
            data_file.write(extracted.read())

