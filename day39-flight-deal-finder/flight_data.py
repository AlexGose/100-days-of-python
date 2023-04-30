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

    def alert_message(self):
        message = f"Low price alert! Only ${self.price} to fly "
        message += f"from {self.city_from}-{self.airport_from} "
        message += f"to {self.city_to}-{self.airport_to} "
        message += f"from {self.departure_date} "
        message += f"to {self.return_date}."
        return message

    @staticmethod
    def parse_json(json):
        return FlightData(json['price'], json['flyFrom'], json['cityFrom'], json['flyTo'], json['cityTo'],
                          json['route'][0]['local_departure'][:10], json['route'][1]['local_arrival'][:10])


if __name__ == '__main__':
    fd = FlightData('41', 'STN', 'London', 'SXF', 'Berlin', '2020-08-25', '2020-09-10')
    print(fd.alert_message())
    print(fd)
