from flight_search import FlightSearch
from data_manager import DataManager


if __name__ == '__main__':
    fs = FlightSearch()
    dm = DataManager()
    for row in dm.get_rows():
        code = fs.get_iata(row['city'])
        print(row['id'], row['city'], code)
