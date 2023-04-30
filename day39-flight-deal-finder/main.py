from flight_search import FlightSearch
from data_manager import DataManager


if __name__ == '__main__':
    fs = FlightSearch()
    dm = DataManager()
    for row in dm.get_rows():
        dm.edit_iata_code(row['id'], fs.get_iata(row['city']))
