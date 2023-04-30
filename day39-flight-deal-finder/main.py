from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import os

DEPARTURE_AIRPORT = os.getenv('DEPARTURE_AIRPORT')

if __name__ == '__main__':
    fs = FlightSearch(DEPARTURE_AIRPORT)
    dm = DataManager()
    rows = dm.get_rows()
    for row in rows:
        iata_code = fs.get_iata(row['city'])
        # dm.edit_iata_code(row['id'], iata_code)
        cheapest_flight = fs.get_cheapest_flight(iata_code, int(row['lowestPrice']))
        if cheapest_flight:
            fd = FlightData.parse_json(cheapest_flight)
            print(fd.alert_message())
