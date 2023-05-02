from dataclasses import dataclass


@dataclass
class FlightData:
    price: str
    airport_from: str
    city_from: str
    airport_to: str
    city_to: str
    departure_date: str
    return_date: str
    stop_overs: str = '0'
    via_city_leave: str = ''
    via_city_return: str = ''

    def alert_message(self):
        message = f"Low price alert! Only ${self.price} to fly "
        message += f"from {self.city_from}-{self.airport_from} "
        message += f"to {self.city_to}-{self.airport_to} "
        message += f"from {self.departure_date} "
        message += f"to {self.return_date}."
        if self.stop_overs == '2':
            message += f"\nFlight has 1 stop over in {self.via_city_leave} (leaving) "
            message += f"and 1 stop over in {self.via_city_return} (returning)"
        return message

    @staticmethod
    def parse_json(json):
        if len(json['route']) == 2:
            return FlightData(json['price'], json['flyFrom'], json['cityFrom'], json['flyTo'], json['cityTo'],
                              json['route'][0]['local_departure'][:10], json['route'][1]['local_arrival'][:10])
        elif len(json['route']) == 4:
            return FlightData(json['price'], json['flyFrom'], json['cityFrom'], json['flyTo'], json['cityTo'],
                              json['route'][0]['local_departure'][:10], json['route'][3]['local_arrival'][:10],
                              '2', json['route'][0]['cityTo'], json['route'][3]['cityFrom'])
        else:
            raise ValueError(f"{len(json['route'])} flights in this itinerary, only 2 or 4 supported.")


if __name__ == '__main__':
    fd = FlightData('41', 'STN', 'London', 'SXF', 'Berlin', '2020-08-25', '2020-09-10')
    print(fd.alert_message())
    print(fd)

    fd2 = FlightData('41', 'STN', 'London', 'DPS', 'Bali', '2020-08-25', '2020-09-10', '2', 'Singapore', 'Dubai')
    print(fd2.alert_message())
    print(fd2)
