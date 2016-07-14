import csv
import sys
from urllib.request import urlopen


def get_capital_data():
    """Return parsed CSV data from capitals API."""
    url = "http://api.geonames.org/countryInfoCSV?username=truthfultechnology"
    with urlopen(url) as response:
        raw_data = response.read().decode('utf-8').splitlines()
        reader = csv.DictReader(raw_data, delimiter="\t")
        return [row for row in reader]


def rearrange_capital_data(old_rows):
    """Sort CSV data by population and rename country column."""
    new_rows = [{
        'country': row['name'],
        'capital': row['capital'],
        'population': row['population'],
    } for row in old_rows]
    return sorted(new_rows, reverse=True, key=lambda r: int(r['population']))


def write_capital_file(file_name, csv_rows):
    """Write capital rows CSV file."""
    headers = ["country", "capital", "population"]
    with open(file_name, mode='wt') as out_file:
        writer = csv.DictWriter(out_file, delimiter=",",
                                fieldnames=headers)
        writer.writeheader()
        writer.writerows(csv_rows)


def main(out_file_name):
    original_data = get_capital_data()
    new_data = rearrange_capital_data(original_data)
    write_capital_file(out_file_name, new_data)


if __name__ == "__main__":
    main(sys.argv[1])
